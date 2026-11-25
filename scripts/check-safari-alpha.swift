import Foundation
import AVFoundation
let asset = AVURLAsset(url:URL(fileURLWithPath:CommandLine.arguments[1]))
let track = asset.tracks(withMediaType:.video)[0]
let reader = try AVAssetReader(asset:asset)
let output = AVAssetReaderTrackOutput(track:track, outputSettings:[kCVPixelBufferPixelFormatTypeKey as String:kCVPixelFormatType_32BGRA])
reader.add(output);reader.startReading()
var frames=0, transparent=0, opaque=0
while let sample=output.copyNextSampleBuffer() {
 let p=CMSampleBufferGetImageBuffer(sample)!
 CVPixelBufferLockBaseAddress(p,.readOnly)
 let bytes=CVPixelBufferGetBaseAddress(p)!.assumingMemoryBound(to:UInt8.self), stride=CVPixelBufferGetBytesPerRow(p)
 if bytes[3] == 0 { transparent += 1 }
 for y in 0..<CVPixelBufferGetHeight(p) { for x in 0..<CVPixelBufferGetWidth(p) { if bytes[y*stride+x*4+3] > 240 { opaque += 1 } } }
 CVPixelBufferUnlockBaseAddress(p,.readOnly);frames += 1
}
print("frames=\(frames) transparentCorners=\(transparent) opaquePixels=\(opaque) duration=\(CMTimeGetSeconds(asset.duration)) status=\(reader.status.rawValue)")
if transparent != frames || opaque == 0 || reader.status != .completed { exit(1) }
