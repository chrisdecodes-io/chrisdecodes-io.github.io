import Foundation
import AVFoundation
import VideoToolbox
let args = CommandLine.arguments
let w = Int(args[1])!, h = Int(args[2])!, output = URL(fileURLWithPath: args[3])
try? FileManager.default.removeItem(at: output)
let writer = try AVAssetWriter(outputURL: output, fileType: .mov)
let input = AVAssetWriterInput(mediaType: .video, outputSettings: [AVVideoCodecKey: AVVideoCodecType.hevcWithAlpha, AVVideoWidthKey:w, AVVideoHeightKey:h, AVVideoCompressionPropertiesKey:[kVTCompressionPropertyKey_TargetQualityForAlpha as String:1.0,kVTCompressionPropertyKey_Quality as String:0.85,kVTCompressionPropertyKey_AlphaChannelMode as String:kVTAlphaChannelMode_StraightAlpha]])
let adapter = AVAssetWriterInputPixelBufferAdaptor(assetWriterInput: input, sourcePixelBufferAttributes:[kCVPixelBufferPixelFormatTypeKey as String:kCVPixelFormatType_32BGRA,kCVPixelBufferWidthKey as String:w,kCVPixelBufferHeightKey as String:h,kCVPixelBufferIOSurfacePropertiesKey as String:[:]])
writer.add(input)
writer.startWriting(); writer.startSession(atSourceTime:.zero)
let done=DispatchSemaphore(value:0), queue=DispatchQueue(label:"encode")
var frame:Int64=0
input.requestMediaDataWhenReady(on:queue) {
 while input.isReadyForMoreMediaData {
  var bytes=Data()
  while bytes.count < w*h*4 {
   let chunk=FileHandle.standardInput.readData(ofLength:w*h*4-bytes.count)
   if chunk.isEmpty { break }; bytes.append(chunk)
  }
  if bytes.isEmpty { input.markAsFinished();writer.finishWriting { done.signal() };return }
  if bytes.count != w*h*4 { fatalError("Incomplete frame") }
  var pixel:CVPixelBuffer?
  CVPixelBufferPoolCreatePixelBuffer(nil,adapter.pixelBufferPool!,&pixel)
  CVPixelBufferLockBaseAddress(pixel!,[])
  let stride=CVPixelBufferGetBytesPerRow(pixel!)
  bytes.withUnsafeBytes { raw in
   for row in 0..<h { memcpy(CVPixelBufferGetBaseAddress(pixel!)!.advanced(by:row*stride),raw.baseAddress!.advanced(by:row*w*4),w*4) }
  }
  CVPixelBufferUnlockBaseAddress(pixel!,[])
  if !adapter.append(pixel!,withPresentationTime:CMTime(value:frame,timescale:30)) { fatalError("Append: \(String(describing:writer.error))") }
  frame += 1
 }
}
done.wait()
if writer.status != .completed { fatalError("Encode: \(String(describing:writer.error))") }
print("Encoded \(frame) frames: \(output.path)")
