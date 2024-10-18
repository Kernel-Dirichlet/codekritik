; ModuleID = 'main.9442b880e418b61e-cgu.0'
source_filename = "main.9442b880e418b61e-cgu.0"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%"core::fmt::rt::Argument<'_>" = type { %"core::fmt::rt::ArgumentType<'_>" }
%"core::fmt::rt::ArgumentType<'_>" = type { [1 x i64], ptr }

@vtable.0 = private constant <{ ptr, [16 x i8], ptr, ptr, ptr }> <{ ptr @"_ZN4core3ptr85drop_in_place$LT$std..rt..lang_start$LT$$LP$$RP$$GT$..$u7b$$u7b$closure$u7d$$u7d$$GT$17h3bd5227b6af50977E", [16 x i8] c"\08\00\00\00\00\00\00\00\08\00\00\00\00\00\00\00", ptr @"_ZN4core3ops8function6FnOnce40call_once$u7b$$u7b$vtable.shim$u7d$$u7d$17ha807470326e2055bE", ptr @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h29cbc39fca137ac4E", ptr @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h29cbc39fca137ac4E" }>, align 8, !dbg !0
@0 = private unnamed_addr constant <{ [8 x i8], [8 x i8] }> <{ [8 x i8] zeroinitializer, [8 x i8] undef }>, align 8
@alloc_91c7fa63c3cfeaa3c795652d5cf060e4 = private unnamed_addr constant <{ [12 x i8] }> <{ [12 x i8] c"invalid args" }>, align 1
@alloc_af99043bc04c419363a7f04d23183506 = private unnamed_addr constant <{ ptr, [8 x i8] }> <{ ptr @alloc_91c7fa63c3cfeaa3c795652d5cf060e4, [8 x i8] c"\0C\00\00\00\00\00\00\00" }>, align 8
@alloc_5aed2bef020d7c04d125725a1bc376e1 = private unnamed_addr constant <{ [64 x i8] }> <{ [64 x i8] c"/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/fmt/mod.rs" }>, align 1
@alloc_3d94d3e5981669d0f1c481d1aa66390f = private unnamed_addr constant <{ ptr, [16 x i8] }> <{ ptr @alloc_5aed2bef020d7c04d125725a1bc376e1, [16 x i8] c"@\00\00\00\00\00\00\00U\01\00\00\0D\00\00\00" }>, align 8
@alloc_4693327ca9c5449cec9b739948ccbb5e = private unnamed_addr constant <{ [7 x i8] }> <{ [7 x i8] c"main.rs" }>, align 1
@alloc_0a33b9b3cd2ae03a9af40e9b98813753 = private unnamed_addr constant <{ ptr, [16 x i8] }> <{ ptr @alloc_4693327ca9c5449cec9b739948ccbb5e, [16 x i8] c"\07\00\00\00\00\00\00\00\04\00\00\00\1C\00\00\00" }>, align 8
@alloc_70105309596e4980ec0ced8de4dc382d = private unnamed_addr constant <{ ptr, [16 x i8] }> <{ ptr @alloc_4693327ca9c5449cec9b739948ccbb5e, [16 x i8] c"\07\00\00\00\00\00\00\00\04\00\00\00\0E\00\00\00" }>, align 8
@alloc_fe43a1b4184176b6c6598343659e46ae = private unnamed_addr constant <{ [13 x i8] }> <{ [13 x i8] c"Factorial of " }>, align 1
@alloc_556e4180596b5b612bb6ed6c0cbb55e1 = private unnamed_addr constant <{ [2 x i8] }> <{ [2 x i8] c": " }>, align 1
@alloc_49a1e817e911805af64bbc7efb390101 = private unnamed_addr constant <{ [1 x i8] }> <{ [1 x i8] c"\0A" }>, align 1
@alloc_8dcbd38cab599c4fbf3011828d08fd1c = private unnamed_addr constant <{ ptr, [8 x i8], ptr, [8 x i8], ptr, [8 x i8] }> <{ ptr @alloc_fe43a1b4184176b6c6598343659e46ae, [8 x i8] c"\0D\00\00\00\00\00\00\00", ptr @alloc_556e4180596b5b612bb6ed6c0cbb55e1, [8 x i8] c"\02\00\00\00\00\00\00\00", ptr @alloc_49a1e817e911805af64bbc7efb390101, [8 x i8] c"\01\00\00\00\00\00\00\00" }>, align 8
@__rustc_debug_gdb_scripts_section__ = linkonce_odr unnamed_addr constant [34 x i8] c"\01gdb_load_rust_pretty_printers.py\00", section ".debug_gdb_scripts", align 1

; std::sys_common::backtrace::__rust_begin_short_backtrace
; Function Attrs: noinline nonlazybind uwtable
define internal void @_ZN3std10sys_common9backtrace28__rust_begin_short_backtrace17h55ac28211f104d26E(ptr %f) unnamed_addr #0 !dbg !44 {
start:
  %f.dbg.spill = alloca [8 x i8], align 8
  %result.dbg.spill = alloca [0 x i8], align 1
  %dummy.dbg.spill = alloca [0 x i8], align 1
  call void @llvm.dbg.declare(metadata ptr %dummy.dbg.spill, metadata !57, metadata !DIExpression()), !dbg !66
  call void @llvm.dbg.declare(metadata ptr %result.dbg.spill, metadata !52, metadata !DIExpression()), !dbg !68
  store ptr %f, ptr %f.dbg.spill, align 8, !dbg !66
  call void @llvm.dbg.declare(metadata ptr %f.dbg.spill, metadata !51, metadata !DIExpression()), !dbg !69
; call core::ops::function::FnOnce::call_once
  call void @_ZN4core3ops8function6FnOnce9call_once17h9bca4dd66ad55774E(ptr %f), !dbg !70
  call void asm sideeffect "", "~{memory}"(), !dbg !71, !srcloc !72
  ret void, !dbg !73
}

; std::rt::lang_start
; Function Attrs: nonlazybind uwtable
define hidden i64 @_ZN3std2rt10lang_start17hae3c394a680aeb0bE(ptr %main, i64 %argc, ptr %argv, i8 %sigpipe) unnamed_addr #1 !dbg !74 {
start:
  %v.dbg.spill = alloca [8 x i8], align 8
  %sigpipe.dbg.spill = alloca [1 x i8], align 1
  %argv.dbg.spill = alloca [8 x i8], align 8
  %argc.dbg.spill = alloca [8 x i8], align 8
  %main.dbg.spill = alloca [8 x i8], align 8
  %_8 = alloca [8 x i8], align 8
  %_5 = alloca [8 x i8], align 8
  store ptr %main, ptr %main.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %main.dbg.spill, metadata !82, metadata !DIExpression()), !dbg !88
  store i64 %argc, ptr %argc.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %argc.dbg.spill, metadata !83, metadata !DIExpression()), !dbg !89
  store ptr %argv, ptr %argv.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %argv.dbg.spill, metadata !84, metadata !DIExpression()), !dbg !90
  store i8 %sigpipe, ptr %sigpipe.dbg.spill, align 1
  call void @llvm.dbg.declare(metadata ptr %sigpipe.dbg.spill, metadata !85, metadata !DIExpression()), !dbg !91
  store ptr %main, ptr %_8, align 8, !dbg !92
; call std::rt::lang_start_internal
  %0 = call i64 @_ZN3std2rt19lang_start_internal17h5add80e16e4e0045E(ptr align 1 %_8, ptr align 8 @vtable.0, i64 %argc, ptr %argv, i8 %sigpipe), !dbg !93
  store i64 %0, ptr %_5, align 8, !dbg !93
  %v = load i64, ptr %_5, align 8, !dbg !94
  store i64 %v, ptr %v.dbg.spill, align 8, !dbg !94
  call void @llvm.dbg.declare(metadata ptr %v.dbg.spill, metadata !86, metadata !DIExpression()), !dbg !95
  ret i64 %v, !dbg !96
}

; std::rt::lang_start::{{closure}}
; Function Attrs: inlinehint nonlazybind uwtable
define internal i32 @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h29cbc39fca137ac4E"(ptr align 8 %_1) unnamed_addr #2 !dbg !97 {
start:
  %self.dbg.spill = alloca [8 x i8], align 8
  %_1.dbg.spill = alloca [8 x i8], align 8
  %self = alloca [1 x i8], align 1
  store ptr %_1, ptr %_1.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %_1.dbg.spill, metadata !103, metadata !DIExpression(DW_OP_deref)), !dbg !104
  call void @llvm.dbg.declare(metadata ptr %self, metadata !105, metadata !DIExpression()), !dbg !125
  %_4 = load ptr, ptr %_1, align 8, !dbg !127
; call std::sys_common::backtrace::__rust_begin_short_backtrace
  call void @_ZN3std10sys_common9backtrace28__rust_begin_short_backtrace17h55ac28211f104d26E(ptr %_4), !dbg !128
; call <() as std::process::Termination>::report
  %0 = call i8 @"_ZN54_$LT$$LP$$RP$$u20$as$u20$std..process..Termination$GT$6report17h365417c523693d0cE"(), !dbg !128
  store i8 %0, ptr %self, align 1, !dbg !128
  store ptr %self, ptr %self.dbg.spill, align 8, !dbg !129
  call void @llvm.dbg.declare(metadata ptr %self.dbg.spill, metadata !130, metadata !DIExpression()), !dbg !139
  %_6 = load i8, ptr %self, align 1, !dbg !141
  %_0 = zext i8 %_6 to i32, !dbg !141
  ret i32 %_0, !dbg !142
}

; core::fmt::num::<impl core::fmt::Debug for u128>::fmt
; Function Attrs: inlinehint nonlazybind uwtable
define internal zeroext i1 @"_ZN4core3fmt3num51_$LT$impl$u20$core..fmt..Debug$u20$for$u20$u128$GT$3fmt17hea52cd7b827b2bdaE"(ptr align 16 %self, ptr align 8 %f) unnamed_addr #2 !dbg !143 {
start:
  %f.dbg.spill = alloca [8 x i8], align 8
  %self.dbg.spill = alloca [8 x i8], align 8
  %_0 = alloca [1 x i8], align 1
  store ptr %self, ptr %self.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %self.dbg.spill, metadata !205, metadata !DIExpression()), !dbg !207
  store ptr %f, ptr %f.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %f.dbg.spill, metadata !206, metadata !DIExpression()), !dbg !208
  call void @llvm.dbg.declare(metadata ptr %f.dbg.spill, metadata !209, metadata !DIExpression()), !dbg !219
  call void @llvm.dbg.declare(metadata ptr %f.dbg.spill, metadata !221, metadata !DIExpression()), !dbg !226
  %0 = getelementptr inbounds i8, ptr %f, i64 52, !dbg !228
  %_4 = load i32, ptr %0, align 4, !dbg !228
  %_3 = and i32 %_4, 16, !dbg !228
  %1 = icmp eq i32 %_3, 0, !dbg !229
  br i1 %1, label %bb2, label %bb1, !dbg !229

bb2:                                              ; preds = %start
  %2 = getelementptr inbounds i8, ptr %f, i64 52, !dbg !230
  %_6 = load i32, ptr %2, align 4, !dbg !230
  %_5 = and i32 %_6, 32, !dbg !230
  %3 = icmp eq i32 %_5, 0, !dbg !231
  br i1 %3, label %bb4, label %bb3, !dbg !231

bb1:                                              ; preds = %start
; call core::fmt::num::<impl core::fmt::LowerHex for u128>::fmt
  %4 = call zeroext i1 @"_ZN4core3fmt3num54_$LT$impl$u20$core..fmt..LowerHex$u20$for$u20$u128$GT$3fmt17hac1d2cfc47d6632eE"(ptr align 16 %self, ptr align 8 %f), !dbg !232
  %5 = zext i1 %4 to i8, !dbg !232
  store i8 %5, ptr %_0, align 1, !dbg !232
  br label %bb6, !dbg !232

bb4:                                              ; preds = %bb2
; call core::fmt::num::<impl core::fmt::Display for u128>::fmt
  %6 = call zeroext i1 @"_ZN4core3fmt3num53_$LT$impl$u20$core..fmt..Display$u20$for$u20$u128$GT$3fmt17h4deb1450aa3af82dE"(ptr align 16 %self, ptr align 8 %f), !dbg !233
  %7 = zext i1 %6 to i8, !dbg !233
  store i8 %7, ptr %_0, align 1, !dbg !233
  br label %bb5, !dbg !233

bb3:                                              ; preds = %bb2
; call core::fmt::num::<impl core::fmt::UpperHex for u128>::fmt
  %8 = call zeroext i1 @"_ZN4core3fmt3num54_$LT$impl$u20$core..fmt..UpperHex$u20$for$u20$u128$GT$3fmt17h24f399747b57a9adE"(ptr align 16 %self, ptr align 8 %f), !dbg !234
  %9 = zext i1 %8 to i8, !dbg !234
  store i8 %9, ptr %_0, align 1, !dbg !234
  br label %bb5, !dbg !234

bb5:                                              ; preds = %bb3, %bb4
  br label %bb6, !dbg !235

bb6:                                              ; preds = %bb1, %bb5
  %10 = load i8, ptr %_0, align 1, !dbg !236
  %11 = trunc i8 %10 to i1, !dbg !236
  ret i1 %11, !dbg !236
}

; core::fmt::Arguments::new_v1
; Function Attrs: inlinehint nonlazybind uwtable
define internal void @_ZN4core3fmt9Arguments6new_v117hc7d70b2a7a10bb03E(ptr sret([48 x i8]) align 8 %_0, ptr align 8 %pieces.0, i64 %pieces.1, ptr align 8 %args.0, i64 %args.1) unnamed_addr #2 !dbg !237 {
start:
  %pieces.dbg.spill1 = alloca [16 x i8], align 8
  %args.dbg.spill = alloca [16 x i8], align 8
  %pieces.dbg.spill = alloca [16 x i8], align 8
  %_9 = alloca [48 x i8], align 8
  store ptr %pieces.0, ptr %pieces.dbg.spill, align 8
  %0 = getelementptr inbounds i8, ptr %pieces.dbg.spill, i64 8
  store i64 %pieces.1, ptr %0, align 8
  call void @llvm.dbg.declare(metadata ptr %pieces.dbg.spill, metadata !326, metadata !DIExpression()), !dbg !328
  store ptr %args.0, ptr %args.dbg.spill, align 8
  %1 = getelementptr inbounds i8, ptr %args.dbg.spill, i64 8
  store i64 %args.1, ptr %1, align 8
  call void @llvm.dbg.declare(metadata ptr %args.dbg.spill, metadata !327, metadata !DIExpression()), !dbg !329
  %_3 = icmp ult i64 %pieces.1, %args.1, !dbg !330
  br i1 %_3, label %bb3, label %bb1, !dbg !330

bb1:                                              ; preds = %start
  %_7 = add i64 %args.1, 1, !dbg !331
  %_6 = icmp ugt i64 %pieces.1, %_7, !dbg !332
  br i1 %_6, label %bb2, label %bb4, !dbg !332

bb3:                                              ; preds = %bb2, %start
  store ptr @alloc_af99043bc04c419363a7f04d23183506, ptr %pieces.dbg.spill1, align 8, !dbg !333
  %2 = getelementptr inbounds i8, ptr %pieces.dbg.spill1, i64 8, !dbg !333
  store i64 1, ptr %2, align 8, !dbg !333
  call void @llvm.dbg.declare(metadata ptr %pieces.dbg.spill1, metadata !334, metadata !DIExpression()), !dbg !341
  store ptr @alloc_af99043bc04c419363a7f04d23183506, ptr %_9, align 8, !dbg !345
  %3 = getelementptr inbounds i8, ptr %_9, i64 8, !dbg !345
  store i64 1, ptr %3, align 8, !dbg !345
  %4 = load ptr, ptr @0, align 8, !dbg !345
  %5 = load i64, ptr getelementptr inbounds (i8, ptr @0, i64 8), align 8, !dbg !345
  %6 = getelementptr inbounds i8, ptr %_9, i64 32, !dbg !345
  store ptr %4, ptr %6, align 8, !dbg !345
  %7 = getelementptr inbounds i8, ptr %6, i64 8, !dbg !345
  store i64 %5, ptr %7, align 8, !dbg !345
  %8 = getelementptr inbounds i8, ptr %_9, i64 16, !dbg !345
  store ptr inttoptr (i64 8 to ptr), ptr %8, align 8, !dbg !345
  %9 = getelementptr inbounds i8, ptr %8, i64 8, !dbg !345
  store i64 0, ptr %9, align 8, !dbg !345
; call core::panicking::panic_fmt
  call void @_ZN4core9panicking9panic_fmt17h10c3ee83b4e55229E(ptr align 8 %_9, ptr align 8 @alloc_3d94d3e5981669d0f1c481d1aa66390f) #8, !dbg !346
  unreachable, !dbg !346

bb4:                                              ; preds = %bb1
  store ptr %pieces.0, ptr %_0, align 8, !dbg !347
  %10 = getelementptr inbounds i8, ptr %_0, i64 8, !dbg !347
  store i64 %pieces.1, ptr %10, align 8, !dbg !347
  %11 = load ptr, ptr @0, align 8, !dbg !347
  %12 = load i64, ptr getelementptr inbounds (i8, ptr @0, i64 8), align 8, !dbg !347
  %13 = getelementptr inbounds i8, ptr %_0, i64 32, !dbg !347
  store ptr %11, ptr %13, align 8, !dbg !347
  %14 = getelementptr inbounds i8, ptr %13, i64 8, !dbg !347
  store i64 %12, ptr %14, align 8, !dbg !347
  %15 = getelementptr inbounds i8, ptr %_0, i64 16, !dbg !347
  store ptr %args.0, ptr %15, align 8, !dbg !347
  %16 = getelementptr inbounds i8, ptr %15, i64 8, !dbg !347
  store i64 %args.1, ptr %16, align 8, !dbg !347
  ret void, !dbg !348

bb2:                                              ; preds = %bb1
  br label %bb3, !dbg !349
}

; core::ops::function::FnOnce::call_once{{vtable.shim}}
; Function Attrs: inlinehint nonlazybind uwtable
define internal i32 @"_ZN4core3ops8function6FnOnce40call_once$u7b$$u7b$vtable.shim$u7d$$u7d$17ha807470326e2055bE"(ptr %_1) unnamed_addr #2 !dbg !350 {
start:
  %_1.dbg.spill = alloca [8 x i8], align 8
  %_2 = alloca [0 x i8], align 1
  store ptr %_1, ptr %_1.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %_1.dbg.spill, metadata !359, metadata !DIExpression()), !dbg !364
  call void @llvm.dbg.declare(metadata ptr %_2, metadata !360, metadata !DIExpression()), !dbg !364
  %0 = load ptr, ptr %_1, align 8, !dbg !364
; call core::ops::function::FnOnce::call_once
  %_0 = call i32 @_ZN4core3ops8function6FnOnce9call_once17h576cf1e5a88dab71E(ptr %0), !dbg !364
  ret i32 %_0, !dbg !364
}

; core::ops::function::FnOnce::call_once
; Function Attrs: inlinehint nonlazybind uwtable
define internal i32 @_ZN4core3ops8function6FnOnce9call_once17h576cf1e5a88dab71E(ptr %0) unnamed_addr #2 personality ptr @rust_eh_personality !dbg !365 {
start:
  %1 = alloca [16 x i8], align 8
  %_2 = alloca [0 x i8], align 1
  %_1 = alloca [8 x i8], align 8
  store ptr %0, ptr %_1, align 8
  call void @llvm.dbg.declare(metadata ptr %_1, metadata !369, metadata !DIExpression()), !dbg !371
  call void @llvm.dbg.declare(metadata ptr %_2, metadata !370, metadata !DIExpression()), !dbg !371
; invoke std::rt::lang_start::{{closure}}
  %_0 = invoke i32 @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h29cbc39fca137ac4E"(ptr align 8 %_1)
          to label %bb1 unwind label %cleanup, !dbg !371

bb3:                                              ; preds = %cleanup
  %2 = load ptr, ptr %1, align 8, !dbg !371
  %3 = getelementptr inbounds i8, ptr %1, i64 8, !dbg !371
  %4 = load i32, ptr %3, align 8, !dbg !371
  %5 = insertvalue { ptr, i32 } poison, ptr %2, 0, !dbg !371
  %6 = insertvalue { ptr, i32 } %5, i32 %4, 1, !dbg !371
  resume { ptr, i32 } %6, !dbg !371

cleanup:                                          ; preds = %start
  %7 = landingpad { ptr, i32 }
          cleanup
  %8 = extractvalue { ptr, i32 } %7, 0
  %9 = extractvalue { ptr, i32 } %7, 1
  store ptr %8, ptr %1, align 8
  %10 = getelementptr inbounds i8, ptr %1, i64 8
  store i32 %9, ptr %10, align 8
  br label %bb3

bb1:                                              ; preds = %start
  ret i32 %_0, !dbg !371
}

; core::ops::function::FnOnce::call_once
; Function Attrs: inlinehint nonlazybind uwtable
define internal void @_ZN4core3ops8function6FnOnce9call_once17h9bca4dd66ad55774E(ptr %_1) unnamed_addr #2 !dbg !372 {
start:
  %_1.dbg.spill = alloca [8 x i8], align 8
  %_2 = alloca [0 x i8], align 1
  store ptr %_1, ptr %_1.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %_1.dbg.spill, metadata !374, metadata !DIExpression()), !dbg !378
  call void @llvm.dbg.declare(metadata ptr %_2, metadata !375, metadata !DIExpression()), !dbg !378
  call void %_1(), !dbg !378
  ret void, !dbg !378
}

; core::ptr::drop_in_place<std::rt::lang_start<()>::{{closure}}>
; Function Attrs: inlinehint nonlazybind uwtable
define internal void @"_ZN4core3ptr85drop_in_place$LT$std..rt..lang_start$LT$$LP$$RP$$GT$..$u7b$$u7b$closure$u7d$$u7d$$GT$17h3bd5227b6af50977E"(ptr align 8 %_1) unnamed_addr #2 !dbg !379 {
start:
  %_1.dbg.spill = alloca [8 x i8], align 8
  store ptr %_1, ptr %_1.dbg.spill, align 8
  call void @llvm.dbg.declare(metadata ptr %_1.dbg.spill, metadata !385, metadata !DIExpression()), !dbg !388
  ret void, !dbg !388
}

; <() as std::process::Termination>::report
; Function Attrs: inlinehint nonlazybind uwtable
define internal i8 @"_ZN54_$LT$$LP$$RP$$u20$as$u20$std..process..Termination$GT$6report17h365417c523693d0cE"() unnamed_addr #2 !dbg !389 {
start:
  %_1.dbg.spill = alloca [0 x i8], align 1
  %self.dbg.spill = alloca [0 x i8], align 1
  call void @llvm.dbg.declare(metadata ptr %self.dbg.spill, metadata !394, metadata !DIExpression()), !dbg !396
  call void @llvm.dbg.declare(metadata ptr %_1.dbg.spill, metadata !395, metadata !DIExpression()), !dbg !396
  ret i8 0, !dbg !397
}

; main::factorial
; Function Attrs: nonlazybind uwtable
define internal i128 @_ZN4main9factorial17h8e596bd882e49064E(i128 %n) unnamed_addr #1 !dbg !398 {
start:
  %n.dbg.spill = alloca [16 x i8], align 16
  %_0 = alloca [16 x i8], align 16
  store i128 %n, ptr %n.dbg.spill, align 16
  call void @llvm.dbg.declare(metadata ptr %n.dbg.spill, metadata !404, metadata !DIExpression()), !dbg !405
  switch i128 %n, label %bb1 [
    i128 0, label %bb2
    i128 1, label %bb2
  ], !dbg !406

bb1:                                              ; preds = %start
  %_4.0 = sub i128 %n, 1, !dbg !407
  %_4.1 = icmp ult i128 %n, 1, !dbg !407
  %0 = call i1 @llvm.expect.i1(i1 %_4.1, i1 false), !dbg !407
  br i1 %0, label %panic, label %bb3, !dbg !407

bb2:                                              ; preds = %start, %start
  store i128 1, ptr %_0, align 16, !dbg !408
  br label %bb6, !dbg !408

bb6:                                              ; preds = %bb5, %bb2
  %1 = load i128, ptr %_0, align 16, !dbg !409
  ret i128 %1, !dbg !409

bb3:                                              ; preds = %bb1
; call main::factorial
  %_2 = call i128 @_ZN4main9factorial17h8e596bd882e49064E(i128 %_4.0), !dbg !410
  %2 = call { i128, i1 } @llvm.umul.with.overflow.i128(i128 %n, i128 %_2), !dbg !411
  %_5.0 = extractvalue { i128, i1 } %2, 0, !dbg !411
  %_5.1 = extractvalue { i128, i1 } %2, 1, !dbg !411
  %3 = call i1 @llvm.expect.i1(i1 %_5.1, i1 false), !dbg !411
  br i1 %3, label %panic1, label %bb5, !dbg !411

panic:                                            ; preds = %bb1
; call core::panicking::panic_const::panic_const_sub_overflow
  call void @_ZN4core9panicking11panic_const24panic_const_sub_overflow17h46b059ebe5394a77E(ptr align 8 @alloc_0a33b9b3cd2ae03a9af40e9b98813753) #8, !dbg !407
  unreachable, !dbg !407

bb5:                                              ; preds = %bb3
  store i128 %_5.0, ptr %_0, align 16, !dbg !411
  br label %bb6, !dbg !412

panic1:                                           ; preds = %bb3
; call core::panicking::panic_const::panic_const_mul_overflow
  call void @_ZN4core9panicking11panic_const24panic_const_mul_overflow17h09e92ca26025b65cE(ptr align 8 @alloc_70105309596e4980ec0ced8de4dc382d) #8, !dbg !411
  unreachable, !dbg !411
}

; main::main
; Function Attrs: nonlazybind uwtable
define internal void @_ZN4main4main17h0ac0b47279fbf2b6E() unnamed_addr #1 !dbg !413 {
start:
  %f.dbg.spill.i1 = alloca [8 x i8], align 8
  %x.dbg.spill.i2 = alloca [8 x i8], align 8
  %_3.i3 = alloca [16 x i8], align 8
  %f.dbg.spill.i = alloca [8 x i8], align 8
  %x.dbg.spill.i = alloca [8 x i8], align 8
  %_3.i = alloca [16 x i8], align 8
  %_12 = alloca [16 x i8], align 16
  %_10 = alloca [16 x i8], align 8
  %_8 = alloca [16 x i8], align 8
  %_7 = alloca [32 x i8], align 8
  %_3 = alloca [48 x i8], align 8
  %_1 = alloca [16 x i8], align 16
  %var1.dbg.spill = alloca [16 x i8], align 16
  store i128 20, ptr %var1.dbg.spill, align 16, !dbg !417
  call void @llvm.dbg.declare(metadata ptr %var1.dbg.spill, metadata !415, metadata !DIExpression()), !dbg !417
  store i128 20, ptr %_1, align 16, !dbg !418
  store ptr %_1, ptr %x.dbg.spill.i, align 8
  call void @llvm.dbg.declare(metadata ptr %x.dbg.spill.i, metadata !419, metadata !DIExpression()), !dbg !428
  call void @llvm.dbg.declare(metadata ptr %x.dbg.spill.i, metadata !430, metadata !DIExpression()), !dbg !439
  store ptr @"_ZN4core3fmt3num53_$LT$impl$u20$core..fmt..Display$u20$for$u20$u128$GT$3fmt17h4deb1450aa3af82dE", ptr %f.dbg.spill.i, align 8, !dbg !441
  call void @llvm.dbg.declare(metadata ptr %f.dbg.spill.i, metadata !438, metadata !DIExpression()), !dbg !442
  store ptr %_1, ptr %_3.i, align 8, !dbg !443
  %0 = getelementptr inbounds i8, ptr %_3.i, i64 8, !dbg !443
  store ptr @"_ZN4core3fmt3num53_$LT$impl$u20$core..fmt..Display$u20$for$u20$u128$GT$3fmt17h4deb1450aa3af82dE", ptr %0, align 8, !dbg !443
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %_8, ptr align 8 %_3.i, i64 16, i1 false), !dbg !444
  %_13 = load i128, ptr %_1, align 16, !dbg !445
; call main::factorial
  %1 = call i128 @_ZN4main9factorial17h8e596bd882e49064E(i128 %_13), !dbg !446
  store i128 %1, ptr %_12, align 16, !dbg !446
  store ptr %_12, ptr %x.dbg.spill.i2, align 8
  call void @llvm.dbg.declare(metadata ptr %x.dbg.spill.i2, metadata !447, metadata !DIExpression()), !dbg !451
  call void @llvm.dbg.declare(metadata ptr %x.dbg.spill.i2, metadata !453, metadata !DIExpression()), !dbg !458
  store ptr @"_ZN4core3fmt3num51_$LT$impl$u20$core..fmt..Debug$u20$for$u20$u128$GT$3fmt17hea52cd7b827b2bdaE", ptr %f.dbg.spill.i1, align 8, !dbg !460
  call void @llvm.dbg.declare(metadata ptr %f.dbg.spill.i1, metadata !457, metadata !DIExpression()), !dbg !461
  store ptr %_12, ptr %_3.i3, align 8, !dbg !462
  %2 = getelementptr inbounds i8, ptr %_3.i3, i64 8, !dbg !462
  store ptr @"_ZN4core3fmt3num51_$LT$impl$u20$core..fmt..Debug$u20$for$u20$u128$GT$3fmt17hea52cd7b827b2bdaE", ptr %2, align 8, !dbg !462
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %_10, ptr align 8 %_3.i3, i64 16, i1 false), !dbg !463
  %3 = getelementptr inbounds [2 x %"core::fmt::rt::Argument<'_>"], ptr %_7, i64 0, i64 0, !dbg !464
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %3, ptr align 8 %_8, i64 16, i1 false), !dbg !464
  %4 = getelementptr inbounds [2 x %"core::fmt::rt::Argument<'_>"], ptr %_7, i64 0, i64 1, !dbg !464
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %4, ptr align 8 %_10, i64 16, i1 false), !dbg !464
; call core::fmt::Arguments::new_v1
  call void @_ZN4core3fmt9Arguments6new_v117hc7d70b2a7a10bb03E(ptr sret([48 x i8]) align 8 %_3, ptr align 8 @alloc_8dcbd38cab599c4fbf3011828d08fd1c, i64 3, ptr align 8 %_7, i64 2), !dbg !464
; call std::io::stdio::_print
  call void @_ZN3std2io5stdio6_print17ha0210d71b2837db0E(ptr align 8 %_3), !dbg !464
  ret void, !dbg !465
}

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare void @llvm.dbg.declare(metadata, metadata, metadata) #3

; std::rt::lang_start_internal
; Function Attrs: nonlazybind uwtable
declare i64 @_ZN3std2rt19lang_start_internal17h5add80e16e4e0045E(ptr align 1, ptr align 8, i64, ptr, i8) unnamed_addr #1

; core::fmt::num::<impl core::fmt::Display for u128>::fmt
; Function Attrs: nonlazybind uwtable
declare zeroext i1 @"_ZN4core3fmt3num53_$LT$impl$u20$core..fmt..Display$u20$for$u20$u128$GT$3fmt17h4deb1450aa3af82dE"(ptr align 16, ptr align 8) unnamed_addr #1

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias nocapture writeonly, ptr noalias nocapture readonly, i64, i1 immarg) #4

; core::fmt::num::<impl core::fmt::UpperHex for u128>::fmt
; Function Attrs: nonlazybind uwtable
declare zeroext i1 @"_ZN4core3fmt3num54_$LT$impl$u20$core..fmt..UpperHex$u20$for$u20$u128$GT$3fmt17h24f399747b57a9adE"(ptr align 16, ptr align 8) unnamed_addr #1

; core::fmt::num::<impl core::fmt::LowerHex for u128>::fmt
; Function Attrs: nonlazybind uwtable
declare zeroext i1 @"_ZN4core3fmt3num54_$LT$impl$u20$core..fmt..LowerHex$u20$for$u20$u128$GT$3fmt17hac1d2cfc47d6632eE"(ptr align 16, ptr align 8) unnamed_addr #1

; core::panicking::panic_fmt
; Function Attrs: cold noinline noreturn nonlazybind uwtable
declare void @_ZN4core9panicking9panic_fmt17h10c3ee83b4e55229E(ptr align 8, ptr align 8) unnamed_addr #5

; Function Attrs: nonlazybind uwtable
declare i32 @rust_eh_personality(i32, i32, i64, ptr, ptr) unnamed_addr #1

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(none)
declare i1 @llvm.expect.i1(i1, i1) #6

; core::panicking::panic_const::panic_const_sub_overflow
; Function Attrs: cold noinline noreturn nonlazybind uwtable
declare void @_ZN4core9panicking11panic_const24panic_const_sub_overflow17h46b059ebe5394a77E(ptr align 8) unnamed_addr #5

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare { i128, i1 } @llvm.umul.with.overflow.i128(i128, i128) #3

; core::panicking::panic_const::panic_const_mul_overflow
; Function Attrs: cold noinline noreturn nonlazybind uwtable
declare void @_ZN4core9panicking11panic_const24panic_const_mul_overflow17h09e92ca26025b65cE(ptr align 8) unnamed_addr #5

; std::io::stdio::_print
; Function Attrs: nonlazybind uwtable
declare void @_ZN3std2io5stdio6_print17ha0210d71b2837db0E(ptr align 8) unnamed_addr #1

; Function Attrs: nonlazybind
define i32 @main(i32 %0, ptr %1) unnamed_addr #7 {
top:
  %2 = load volatile i8, ptr @__rustc_debug_gdb_scripts_section__, align 1
  %3 = sext i32 %0 to i64
; call std::rt::lang_start
  %4 = call i64 @_ZN3std2rt10lang_start17hae3c394a680aeb0bE(ptr @_ZN4main4main17h0ac0b47279fbf2b6E, i64 %3, ptr %1, i8 0)
  %5 = trunc i64 %4 to i32
  ret i32 %5
}

attributes #0 = { noinline nonlazybind uwtable "probe-stack"="inline-asm" "target-cpu"="x86-64" }
attributes #1 = { nonlazybind uwtable "probe-stack"="inline-asm" "target-cpu"="x86-64" }
attributes #2 = { inlinehint nonlazybind uwtable "probe-stack"="inline-asm" "target-cpu"="x86-64" }
attributes #3 = { nocallback nofree nosync nounwind speculatable willreturn memory(none) }
attributes #4 = { nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #5 = { cold noinline noreturn nonlazybind uwtable "probe-stack"="inline-asm" "target-cpu"="x86-64" }
attributes #6 = { nocallback nofree nosync nounwind willreturn memory(none) }
attributes #7 = { nonlazybind "target-cpu"="x86-64" }
attributes #8 = { noreturn }

!llvm.module.flags = !{!24, !25, !26, !27, !28}
!llvm.ident = !{!29}
!llvm.dbg.cu = !{!30}

!0 = !DIGlobalVariableExpression(var: !1, expr: !DIExpression())
!1 = distinct !DIGlobalVariable(name: "<std::rt::lang_start::{closure_env#0}<()> as core::ops::function::Fn<()>>::{vtable}", scope: null, file: !2, type: !3, isLocal: true, isDefinition: true)
!2 = !DIFile(filename: "<unknown>", directory: "")
!3 = !DICompositeType(tag: DW_TAG_structure_type, name: "<std::rt::lang_start::{closure_env#0}<()> as core::ops::function::Fn<()>>::{vtable_type}", file: !2, size: 384, align: 64, flags: DIFlagArtificial, elements: !4, vtableHolder: !14, templateParams: !23, identifier: "7822297ee4fbb26886b70417b471398b")
!4 = !{!5, !8, !10, !11, !12, !13}
!5 = !DIDerivedType(tag: DW_TAG_member, name: "drop_in_place", scope: !3, file: !2, baseType: !6, size: 64, align: 64)
!6 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "*const ()", baseType: !7, size: 64, align: 64, dwarfAddressSpace: 0)
!7 = !DIBasicType(name: "()", encoding: DW_ATE_unsigned)
!8 = !DIDerivedType(tag: DW_TAG_member, name: "size", scope: !3, file: !2, baseType: !9, size: 64, align: 64, offset: 64)
!9 = !DIBasicType(name: "usize", size: 64, encoding: DW_ATE_unsigned)
!10 = !DIDerivedType(tag: DW_TAG_member, name: "align", scope: !3, file: !2, baseType: !9, size: 64, align: 64, offset: 128)
!11 = !DIDerivedType(tag: DW_TAG_member, name: "__method3", scope: !3, file: !2, baseType: !6, size: 64, align: 64, offset: 192)
!12 = !DIDerivedType(tag: DW_TAG_member, name: "__method4", scope: !3, file: !2, baseType: !6, size: 64, align: 64, offset: 256)
!13 = !DIDerivedType(tag: DW_TAG_member, name: "__method5", scope: !3, file: !2, baseType: !6, size: 64, align: 64, offset: 320)
!14 = !DICompositeType(tag: DW_TAG_structure_type, name: "{closure_env#0}<()>", scope: !15, file: !2, size: 64, align: 64, elements: !18, templateParams: !23, identifier: "4c4d1d6696bc9c0c11217e1a7a8fac1e")
!15 = !DINamespace(name: "lang_start", scope: !16)
!16 = !DINamespace(name: "rt", scope: !17)
!17 = !DINamespace(name: "std", scope: null)
!18 = !{!19}
!19 = !DIDerivedType(tag: DW_TAG_member, name: "main", scope: !14, file: !2, baseType: !20, size: 64, align: 64)
!20 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "fn()", baseType: !21, size: 64, align: 64, dwarfAddressSpace: 0)
!21 = !DISubroutineType(types: !22)
!22 = !{null}
!23 = !{}
!24 = !{i32 8, !"PIC Level", i32 2}
!25 = !{i32 7, !"PIE Level", i32 2}
!26 = !{i32 2, !"RtLibUseGOT", i32 1}
!27 = !{i32 2, !"Dwarf Version", i32 4}
!28 = !{i32 2, !"Debug Info Version", i32 3}
!29 = !{!"rustc version 1.79.0 (129f3b996 2024-06-10) (Arch Linux rust 1:1.79.0-3)"}
!30 = distinct !DICompileUnit(language: DW_LANG_Rust, file: !31, producer: "clang LLVM (rustc version 1.79.0 (129f3b996 2024-06-10) (Arch Linux rust 1:1.79.0-3))", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !32, globals: !43, splitDebugInlining: false, nameTableKind: None)
!31 = !DIFile(filename: "main.rs/@/main.9442b880e418b61e-cgu.0", directory: "/home/admin/Documents/codemetrics/software_metrics/run_metrics/rust_examples/src")
!32 = !{!33}
!33 = !DICompositeType(tag: DW_TAG_enumeration_type, name: "Alignment", scope: !34, file: !2, baseType: !37, size: 8, align: 8, flags: DIFlagEnumClass, elements: !38)
!34 = !DINamespace(name: "rt", scope: !35)
!35 = !DINamespace(name: "fmt", scope: !36)
!36 = !DINamespace(name: "core", scope: null)
!37 = !DIBasicType(name: "u8", size: 8, encoding: DW_ATE_unsigned)
!38 = !{!39, !40, !41, !42}
!39 = !DIEnumerator(name: "Left", value: 0, isUnsigned: true)
!40 = !DIEnumerator(name: "Right", value: 1, isUnsigned: true)
!41 = !DIEnumerator(name: "Center", value: 2, isUnsigned: true)
!42 = !DIEnumerator(name: "Unknown", value: 3, isUnsigned: true)
!43 = !{!0}
!44 = distinct !DISubprogram(name: "__rust_begin_short_backtrace<fn(), ()>", linkageName: "_ZN3std10sys_common9backtrace28__rust_begin_short_backtrace17h55ac28211f104d26E", scope: !46, file: !45, line: 151, type: !48, scopeLine: 151, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !54, retainedNodes: !50)
!45 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/std/src/sys_common/backtrace.rs", directory: "", checksumkind: CSK_MD5, checksum: "9a938a0945aa66d12453850743d3bf49")
!46 = !DINamespace(name: "backtrace", scope: !47)
!47 = !DINamespace(name: "sys_common", scope: !17)
!48 = !DISubroutineType(types: !49)
!49 = !{null, !20}
!50 = !{!51, !52}
!51 = !DILocalVariable(name: "f", arg: 1, scope: !44, file: !45, line: 151, type: !20)
!52 = !DILocalVariable(name: "result", scope: !53, file: !45, line: 155, type: !7, align: 1)
!53 = distinct !DILexicalBlock(scope: !44, file: !45, line: 155, column: 5)
!54 = !{!55, !56}
!55 = !DITemplateTypeParameter(name: "F", type: !20)
!56 = !DITemplateTypeParameter(name: "T", type: !7)
!57 = !DILocalVariable(name: "dummy", scope: !58, file: !59, line: 337, type: !7, align: 1)
!58 = distinct !DILexicalBlock(scope: !60, file: !59, line: 337, column: 1)
!59 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/hint.rs", directory: "", checksumkind: CSK_MD5, checksum: "36624a7f44e0e372094a9874489ad080")
!60 = distinct !DISubprogram(name: "black_box<()>", linkageName: "_ZN4core4hint9black_box17he3f81f2f71ef119cE", scope: !61, file: !59, line: 337, type: !62, scopeLine: 337, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !65, retainedNodes: !64)
!61 = !DINamespace(name: "hint", scope: !36)
!62 = !DISubroutineType(types: !63)
!63 = !{null, !7}
!64 = !{!57}
!65 = !{!56}
!66 = !DILocation(line: 337, column: 27, scope: !58, inlinedAt: !67)
!67 = !DILocation(line: 158, column: 5, scope: !53)
!68 = !DILocation(line: 155, column: 9, scope: !53)
!69 = !DILocation(line: 151, column: 43, scope: !44)
!70 = !DILocation(line: 155, column: 18, scope: !44)
!71 = !DILocation(line: 338, column: 5, scope: !58, inlinedAt: !67)
!72 = !{i32 1795772}
!73 = !DILocation(line: 161, column: 2, scope: !44)
!74 = distinct !DISubprogram(name: "lang_start<()>", linkageName: "_ZN3std2rt10lang_start17hae3c394a680aeb0bE", scope: !16, file: !75, line: 152, type: !76, scopeLine: 152, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !65, retainedNodes: !81)
!75 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/std/src/rt.rs", directory: "", checksumkind: CSK_MD5, checksum: "0299751eafd3dc46c76db969c1f17154")
!76 = !DISubroutineType(types: !77)
!77 = !{!78, !20, !78, !79, !37}
!78 = !DIBasicType(name: "isize", size: 64, encoding: DW_ATE_signed)
!79 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "*const *const u8", baseType: !80, size: 64, align: 64, dwarfAddressSpace: 0)
!80 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "*const u8", baseType: !37, size: 64, align: 64, dwarfAddressSpace: 0)
!81 = !{!82, !83, !84, !85, !86}
!82 = !DILocalVariable(name: "main", arg: 1, scope: !74, file: !75, line: 153, type: !20)
!83 = !DILocalVariable(name: "argc", arg: 2, scope: !74, file: !75, line: 154, type: !78)
!84 = !DILocalVariable(name: "argv", arg: 3, scope: !74, file: !75, line: 155, type: !79)
!85 = !DILocalVariable(name: "sigpipe", arg: 4, scope: !74, file: !75, line: 156, type: !37)
!86 = !DILocalVariable(name: "v", scope: !87, file: !75, line: 158, type: !78, align: 8)
!87 = distinct !DILexicalBlock(scope: !74, file: !75, line: 158, column: 5)
!88 = !DILocation(line: 153, column: 5, scope: !74)
!89 = !DILocation(line: 154, column: 5, scope: !74)
!90 = !DILocation(line: 155, column: 5, scope: !74)
!91 = !DILocation(line: 156, column: 5, scope: !74)
!92 = !DILocation(line: 159, column: 10, scope: !74)
!93 = !DILocation(line: 158, column: 17, scope: !74)
!94 = !DILocation(line: 158, column: 12, scope: !74)
!95 = !DILocation(line: 158, column: 12, scope: !87)
!96 = !DILocation(line: 165, column: 2, scope: !74)
!97 = distinct !DISubprogram(name: "{closure#0}<()>", linkageName: "_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h29cbc39fca137ac4E", scope: !15, file: !75, line: 159, type: !98, scopeLine: 159, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !65, retainedNodes: !102)
!98 = !DISubroutineType(types: !99)
!99 = !{!100, !101}
!100 = !DIBasicType(name: "i32", size: 32, encoding: DW_ATE_signed)
!101 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "&std::rt::lang_start::{closure_env#0}<()>", baseType: !14, size: 64, align: 64, dwarfAddressSpace: 0)
!102 = !{!103}
!103 = !DILocalVariable(name: "main", scope: !97, file: !75, line: 153, type: !20, align: 8)
!104 = !DILocation(line: 153, column: 5, scope: !97)
!105 = !DILocalVariable(name: "self", arg: 1, scope: !106, file: !107, line: 2038, type: !109)
!106 = distinct !DILexicalBlock(scope: !108, file: !107, line: 2038, column: 5)
!107 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/std/src/process.rs", directory: "", checksumkind: CSK_MD5, checksum: "03fea2b6bc94c1eee51bf80e2b638905")
!108 = distinct !DISubprogram(name: "to_i32", linkageName: "_ZN3std7process8ExitCode6to_i3217h7d68d49d42022e98E", scope: !109, file: !107, line: 2038, type: !121, scopeLine: 2038, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, declaration: !123, retainedNodes: !124)
!109 = !DICompositeType(tag: DW_TAG_structure_type, name: "ExitCode", scope: !110, file: !2, size: 8, align: 8, flags: DIFlagPublic, elements: !111, templateParams: !23, identifier: "5fabc4b87570b6b0705f612f3eabc38a")
!110 = !DINamespace(name: "process", scope: !17)
!111 = !{!112}
!112 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !109, file: !2, baseType: !113, size: 8, align: 8, flags: DIFlagPrivate)
!113 = !DICompositeType(tag: DW_TAG_structure_type, name: "ExitCode", scope: !114, file: !2, size: 8, align: 8, flags: DIFlagPublic, elements: !119, templateParams: !23, identifier: "9a6029e0b170420ca0bd0c26379fc77c")
!114 = !DINamespace(name: "process_common", scope: !115)
!115 = !DINamespace(name: "process", scope: !116)
!116 = !DINamespace(name: "unix", scope: !117)
!117 = !DINamespace(name: "pal", scope: !118)
!118 = !DINamespace(name: "sys", scope: !17)
!119 = !{!120}
!120 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !113, file: !2, baseType: !37, size: 8, align: 8, flags: DIFlagPrivate)
!121 = !DISubroutineType(types: !122)
!122 = !{!100, !109}
!123 = !DISubprogram(name: "to_i32", linkageName: "_ZN3std7process8ExitCode6to_i3217h7d68d49d42022e98E", scope: !109, file: !107, line: 2038, type: !121, scopeLine: 2038, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !23)
!124 = !{!105}
!125 = !DILocation(line: 2038, column: 19, scope: !106, inlinedAt: !126)
!126 = !DILocation(line: 159, column: 92, scope: !97)
!127 = !DILocation(line: 159, column: 77, scope: !97)
!128 = !DILocation(line: 159, column: 18, scope: !97)
!129 = !DILocation(line: 2039, column: 9, scope: !106, inlinedAt: !126)
!130 = !DILocalVariable(name: "self", arg: 1, scope: !131, file: !132, line: 638, type: !136)
!131 = distinct !DILexicalBlock(scope: !133, file: !132, line: 638, column: 5)
!132 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/std/src/sys/pal/unix/process/process_common.rs", directory: "", checksumkind: CSK_MD5, checksum: "f12d6cc5fbe6e47291b02b1d467e8da3")
!133 = distinct !DISubprogram(name: "as_i32", linkageName: "_ZN3std3sys3pal4unix7process14process_common8ExitCode6as_i3217h1f0c97f14362ac12E", scope: !113, file: !132, line: 638, type: !134, scopeLine: 638, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, declaration: !137, retainedNodes: !138)
!134 = !DISubroutineType(types: !135)
!135 = !{!100, !136}
!136 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "&std::sys::pal::unix::process::process_common::ExitCode", baseType: !113, size: 64, align: 64, dwarfAddressSpace: 0)
!137 = !DISubprogram(name: "as_i32", linkageName: "_ZN3std3sys3pal4unix7process14process_common8ExitCode6as_i3217h1f0c97f14362ac12E", scope: !113, file: !132, line: 638, type: !134, scopeLine: 638, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !23)
!138 = !{!130}
!139 = !DILocation(line: 638, column: 19, scope: !131, inlinedAt: !140)
!140 = !DILocation(line: 2039, column: 16, scope: !106, inlinedAt: !126)
!141 = !DILocation(line: 639, column: 9, scope: !131, inlinedAt: !140)
!142 = !DILocation(line: 159, column: 100, scope: !97)
!143 = distinct !DISubprogram(name: "fmt", linkageName: "_ZN4core3fmt3num51_$LT$impl$u20$core..fmt..Debug$u20$for$u20$u128$GT$3fmt17hea52cd7b827b2bdaE", scope: !145, file: !144, line: 189, type: !147, scopeLine: 189, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, retainedNodes: !204)
!144 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/fmt/num.rs", directory: "", checksumkind: CSK_MD5, checksum: "e54845ef989d12b8a79056a0477bb701")
!145 = !DINamespace(name: "{impl#88}", scope: !146)
!146 = !DINamespace(name: "num", scope: !35)
!147 = !DISubroutineType(types: !148)
!148 = !{!149, !166, !168}
!149 = !DICompositeType(tag: DW_TAG_structure_type, name: "Result<(), core::fmt::Error>", scope: !150, file: !2, size: 8, align: 8, flags: DIFlagPublic, elements: !151, templateParams: !23, identifier: "43ab18ed3bf4403d5ae8bf7c53776933")
!150 = !DINamespace(name: "result", scope: !36)
!151 = !{!152}
!152 = !DICompositeType(tag: DW_TAG_variant_part, scope: !149, file: !2, size: 8, align: 8, elements: !153, templateParams: !23, identifier: "c5ada7f043d61b0a4b4bae1083c7f069", discriminator: !165)
!153 = !{!154, !161}
!154 = !DIDerivedType(tag: DW_TAG_member, name: "Ok", scope: !152, file: !2, baseType: !155, size: 8, align: 8, extraData: i128 0)
!155 = !DICompositeType(tag: DW_TAG_structure_type, name: "Ok", scope: !149, file: !2, size: 8, align: 8, flags: DIFlagPublic, elements: !156, templateParams: !158, identifier: "d70373ae90b0bb5dd8c8eb42d478dff2")
!156 = !{!157}
!157 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !155, file: !2, baseType: !7, align: 8, offset: 8, flags: DIFlagPublic)
!158 = !{!56, !159}
!159 = !DITemplateTypeParameter(name: "E", type: !160)
!160 = !DICompositeType(tag: DW_TAG_structure_type, name: "Error", scope: !35, file: !2, align: 8, flags: DIFlagPublic, elements: !23, identifier: "f4c7594878c8bf873fe594c34c714973")
!161 = !DIDerivedType(tag: DW_TAG_member, name: "Err", scope: !152, file: !2, baseType: !162, size: 8, align: 8, extraData: i128 1)
!162 = !DICompositeType(tag: DW_TAG_structure_type, name: "Err", scope: !149, file: !2, size: 8, align: 8, flags: DIFlagPublic, elements: !163, templateParams: !158, identifier: "7b724a0b30e174dd32fbeeb93a249926")
!163 = !{!164}
!164 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !162, file: !2, baseType: !160, align: 8, offset: 8, flags: DIFlagPublic)
!165 = !DIDerivedType(tag: DW_TAG_member, scope: !149, file: !2, baseType: !37, size: 8, align: 8, flags: DIFlagArtificial)
!166 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "&u128", baseType: !167, size: 64, align: 64, dwarfAddressSpace: 0)
!167 = !DIBasicType(name: "u128", size: 128, encoding: DW_ATE_unsigned)
!168 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "&mut core::fmt::Formatter", baseType: !169, size: 64, align: 64, dwarfAddressSpace: 0)
!169 = !DICompositeType(tag: DW_TAG_structure_type, name: "Formatter", scope: !35, file: !2, size: 512, align: 64, flags: DIFlagPublic, elements: !170, templateParams: !23, identifier: "2a141adae2398ac95fcb274d37a85dec")
!170 = !{!171, !173, !175, !176, !192, !193}
!171 = !DIDerivedType(tag: DW_TAG_member, name: "flags", scope: !169, file: !2, baseType: !172, size: 32, align: 32, offset: 416, flags: DIFlagPrivate)
!172 = !DIBasicType(name: "u32", size: 32, encoding: DW_ATE_unsigned)
!173 = !DIDerivedType(tag: DW_TAG_member, name: "fill", scope: !169, file: !2, baseType: !174, size: 32, align: 32, offset: 384, flags: DIFlagPrivate)
!174 = !DIBasicType(name: "char", size: 32, encoding: DW_ATE_UTF)
!175 = !DIDerivedType(tag: DW_TAG_member, name: "align", scope: !169, file: !2, baseType: !33, size: 8, align: 8, offset: 448, flags: DIFlagPrivate)
!176 = !DIDerivedType(tag: DW_TAG_member, name: "width", scope: !169, file: !2, baseType: !177, size: 128, align: 64, flags: DIFlagPrivate)
!177 = !DICompositeType(tag: DW_TAG_structure_type, name: "Option<usize>", scope: !178, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !179, templateParams: !23, identifier: "1fbb51fa7ae873e67484ad9178d07bbc")
!178 = !DINamespace(name: "option", scope: !36)
!179 = !{!180}
!180 = !DICompositeType(tag: DW_TAG_variant_part, scope: !177, file: !2, size: 128, align: 64, elements: !181, templateParams: !23, identifier: "89c5c215db116d99d373ecbc8849003d", discriminator: !190)
!181 = !{!182, !186}
!182 = !DIDerivedType(tag: DW_TAG_member, name: "None", scope: !180, file: !2, baseType: !183, size: 128, align: 64, extraData: i128 0)
!183 = !DICompositeType(tag: DW_TAG_structure_type, name: "None", scope: !177, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !23, templateParams: !184, identifier: "be4fcdae3dd2e9ddc3969dd774f818af")
!184 = !{!185}
!185 = !DITemplateTypeParameter(name: "T", type: !9)
!186 = !DIDerivedType(tag: DW_TAG_member, name: "Some", scope: !180, file: !2, baseType: !187, size: 128, align: 64, extraData: i128 1)
!187 = !DICompositeType(tag: DW_TAG_structure_type, name: "Some", scope: !177, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !188, templateParams: !184, identifier: "f2c935119141c1351865572ba5fda036")
!188 = !{!189}
!189 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !187, file: !2, baseType: !9, size: 64, align: 64, offset: 64, flags: DIFlagPublic)
!190 = !DIDerivedType(tag: DW_TAG_member, scope: !177, file: !2, baseType: !191, size: 64, align: 64, flags: DIFlagArtificial)
!191 = !DIBasicType(name: "u64", size: 64, encoding: DW_ATE_unsigned)
!192 = !DIDerivedType(tag: DW_TAG_member, name: "precision", scope: !169, file: !2, baseType: !177, size: 128, align: 64, offset: 128, flags: DIFlagPrivate)
!193 = !DIDerivedType(tag: DW_TAG_member, name: "buf", scope: !169, file: !2, baseType: !194, size: 128, align: 64, offset: 256, flags: DIFlagPrivate)
!194 = !DICompositeType(tag: DW_TAG_structure_type, name: "&mut dyn core::fmt::Write", file: !2, size: 128, align: 64, elements: !195, templateParams: !23, identifier: "63542d85f7ae40931be2d3f803be77ce")
!195 = !{!196, !199}
!196 = !DIDerivedType(tag: DW_TAG_member, name: "pointer", scope: !194, file: !2, baseType: !197, size: 64, align: 64)
!197 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !198, size: 64, align: 64, dwarfAddressSpace: 0)
!198 = !DICompositeType(tag: DW_TAG_structure_type, name: "dyn core::fmt::Write", file: !2, align: 8, elements: !23, identifier: "c6def317cfccc2141a0de7266264d546")
!199 = !DIDerivedType(tag: DW_TAG_member, name: "vtable", scope: !194, file: !2, baseType: !200, size: 64, align: 64, offset: 64)
!200 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "&[usize; 3]", baseType: !201, size: 64, align: 64, dwarfAddressSpace: 0)
!201 = !DICompositeType(tag: DW_TAG_array_type, baseType: !9, size: 192, align: 64, elements: !202)
!202 = !{!203}
!203 = !DISubrange(count: 3, lowerBound: 0)
!204 = !{!205, !206}
!205 = !DILocalVariable(name: "self", arg: 1, scope: !143, file: !144, line: 189, type: !166)
!206 = !DILocalVariable(name: "f", arg: 2, scope: !143, file: !144, line: 189, type: !168)
!207 = !DILocation(line: 189, column: 20, scope: !143)
!208 = !DILocation(line: 189, column: 27, scope: !143)
!209 = !DILocalVariable(name: "self", arg: 1, scope: !210, file: !211, line: 1896, type: !168)
!210 = distinct !DILexicalBlock(scope: !212, file: !211, line: 1896, column: 5)
!211 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/fmt/mod.rs", directory: "", checksumkind: CSK_MD5, checksum: "a8c8ff13cf0d35b2c1e2758196da2e38")
!212 = distinct !DISubprogram(name: "debug_lower_hex", linkageName: "_ZN4core3fmt9Formatter15debug_lower_hex17hdfe5bbf15b9b0666E", scope: !169, file: !211, line: 1896, type: !213, scopeLine: 1896, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, declaration: !217, retainedNodes: !218)
!213 = !DISubroutineType(types: !214)
!214 = !{!215, !216}
!215 = !DIBasicType(name: "bool", size: 8, encoding: DW_ATE_boolean)
!216 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "&core::fmt::Formatter", baseType: !169, size: 64, align: 64, dwarfAddressSpace: 0)
!217 = !DISubprogram(name: "debug_lower_hex", linkageName: "_ZN4core3fmt9Formatter15debug_lower_hex17hdfe5bbf15b9b0666E", scope: !169, file: !211, line: 1896, type: !213, scopeLine: 1896, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !23)
!218 = !{!209}
!219 = !DILocation(line: 1896, column: 24, scope: !210, inlinedAt: !220)
!220 = !DILocation(line: 190, column: 22, scope: !143)
!221 = !DILocalVariable(name: "self", arg: 1, scope: !222, file: !211, line: 1900, type: !168)
!222 = distinct !DILexicalBlock(scope: !223, file: !211, line: 1900, column: 5)
!223 = distinct !DISubprogram(name: "debug_upper_hex", linkageName: "_ZN4core3fmt9Formatter15debug_upper_hex17h598ca1b2cd9ba82fE", scope: !169, file: !211, line: 1900, type: !213, scopeLine: 1900, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, declaration: !224, retainedNodes: !225)
!224 = !DISubprogram(name: "debug_upper_hex", linkageName: "_ZN4core3fmt9Formatter15debug_upper_hex17h598ca1b2cd9ba82fE", scope: !169, file: !211, line: 1900, type: !213, scopeLine: 1900, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !23)
!225 = !{!221}
!226 = !DILocation(line: 1900, column: 24, scope: !222, inlinedAt: !227)
!227 = !DILocation(line: 192, column: 29, scope: !143)
!228 = !DILocation(line: 1897, column: 9, scope: !210, inlinedAt: !220)
!229 = !DILocation(line: 190, column: 20, scope: !143)
!230 = !DILocation(line: 1901, column: 9, scope: !222, inlinedAt: !227)
!231 = !DILocation(line: 192, column: 27, scope: !143)
!232 = !DILocation(line: 191, column: 21, scope: !143)
!233 = !DILocation(line: 195, column: 21, scope: !143)
!234 = !DILocation(line: 193, column: 21, scope: !143)
!235 = !DILocation(line: 190, column: 17, scope: !143)
!236 = !DILocation(line: 197, column: 14, scope: !143)
!237 = distinct !DISubprogram(name: "new_v1", linkageName: "_ZN4core3fmt9Arguments6new_v117hc7d70b2a7a10bb03E", scope: !238, file: !211, line: 339, type: !322, scopeLine: 339, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, declaration: !324, retainedNodes: !325)
!238 = !DICompositeType(tag: DW_TAG_structure_type, name: "Arguments", scope: !35, file: !2, size: 384, align: 64, flags: DIFlagPublic, elements: !239, templateParams: !23, identifier: "cbde4c4f453586aff6ac734343eef5ba")
!239 = !{!240, !251, !293}
!240 = !DIDerivedType(tag: DW_TAG_member, name: "pieces", scope: !238, file: !2, baseType: !241, size: 128, align: 64, flags: DIFlagPrivate)
!241 = !DICompositeType(tag: DW_TAG_structure_type, name: "&[&str]", file: !2, size: 128, align: 64, elements: !242, templateParams: !23, identifier: "4e66b00a376d6af5b8765440fb2839f")
!242 = !{!243, !250}
!243 = !DIDerivedType(tag: DW_TAG_member, name: "data_ptr", scope: !241, file: !2, baseType: !244, size: 64, align: 64)
!244 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !245, size: 64, align: 64, dwarfAddressSpace: 0)
!245 = !DICompositeType(tag: DW_TAG_structure_type, name: "&str", file: !2, size: 128, align: 64, elements: !246, templateParams: !23, identifier: "9277eecd40495f85161460476aacc992")
!246 = !{!247, !249}
!247 = !DIDerivedType(tag: DW_TAG_member, name: "data_ptr", scope: !245, file: !2, baseType: !248, size: 64, align: 64)
!248 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !37, size: 64, align: 64, dwarfAddressSpace: 0)
!249 = !DIDerivedType(tag: DW_TAG_member, name: "length", scope: !245, file: !2, baseType: !9, size: 64, align: 64, offset: 64)
!250 = !DIDerivedType(tag: DW_TAG_member, name: "length", scope: !241, file: !2, baseType: !9, size: 64, align: 64, offset: 64)
!251 = !DIDerivedType(tag: DW_TAG_member, name: "fmt", scope: !238, file: !2, baseType: !252, size: 128, align: 64, offset: 256, flags: DIFlagPrivate)
!252 = !DICompositeType(tag: DW_TAG_structure_type, name: "Option<&[core::fmt::rt::Placeholder]>", scope: !178, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !253, templateParams: !23, identifier: "4d548b98284a81e7b7cc241f6c854817")
!253 = !{!254}
!254 = !DICompositeType(tag: DW_TAG_variant_part, scope: !252, file: !2, size: 128, align: 64, elements: !255, templateParams: !23, identifier: "c6e51a1cfe1cc6506e2967323ac25b6e", discriminator: !292)
!255 = !{!256, !288}
!256 = !DIDerivedType(tag: DW_TAG_member, name: "None", scope: !254, file: !2, baseType: !257, size: 128, align: 64, extraData: i128 0)
!257 = !DICompositeType(tag: DW_TAG_structure_type, name: "None", scope: !252, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !23, templateParams: !258, identifier: "1484b689bb617b8ceabc3ebfab28263b")
!258 = !{!259}
!259 = !DITemplateTypeParameter(name: "T", type: !260)
!260 = !DICompositeType(tag: DW_TAG_structure_type, name: "&[core::fmt::rt::Placeholder]", file: !2, size: 128, align: 64, elements: !261, templateParams: !23, identifier: "cc459aa5677945afe2777617aea0f190")
!261 = !{!262, !287}
!262 = !DIDerivedType(tag: DW_TAG_member, name: "data_ptr", scope: !260, file: !2, baseType: !263, size: 64, align: 64)
!263 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !264, size: 64, align: 64, dwarfAddressSpace: 0)
!264 = !DICompositeType(tag: DW_TAG_structure_type, name: "Placeholder", scope: !34, file: !2, size: 448, align: 64, flags: DIFlagPublic, elements: !265, templateParams: !23, identifier: "6d535d73038fa7df98fb52a1b96826db")
!265 = !{!266, !267, !268, !269, !270, !286}
!266 = !DIDerivedType(tag: DW_TAG_member, name: "position", scope: !264, file: !2, baseType: !9, size: 64, align: 64, offset: 256, flags: DIFlagPublic)
!267 = !DIDerivedType(tag: DW_TAG_member, name: "fill", scope: !264, file: !2, baseType: !174, size: 32, align: 32, offset: 320, flags: DIFlagPublic)
!268 = !DIDerivedType(tag: DW_TAG_member, name: "align", scope: !264, file: !2, baseType: !33, size: 8, align: 8, offset: 384, flags: DIFlagPublic)
!269 = !DIDerivedType(tag: DW_TAG_member, name: "flags", scope: !264, file: !2, baseType: !172, size: 32, align: 32, offset: 352, flags: DIFlagPublic)
!270 = !DIDerivedType(tag: DW_TAG_member, name: "precision", scope: !264, file: !2, baseType: !271, size: 128, align: 64, flags: DIFlagPublic)
!271 = !DICompositeType(tag: DW_TAG_structure_type, name: "Count", scope: !34, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !272, templateParams: !23, identifier: "6ddcb40d5a7e0c3da9d4386d80136c75")
!272 = !{!273}
!273 = !DICompositeType(tag: DW_TAG_variant_part, scope: !271, file: !2, size: 128, align: 64, elements: !274, templateParams: !23, identifier: "def4dbbcc5ede411f4c04d3e0977d322", discriminator: !285)
!274 = !{!275, !279, !283}
!275 = !DIDerivedType(tag: DW_TAG_member, name: "Is", scope: !273, file: !2, baseType: !276, size: 128, align: 64, extraData: i128 0)
!276 = !DICompositeType(tag: DW_TAG_structure_type, name: "Is", scope: !271, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !277, templateParams: !23, identifier: "d8484f9e91a37e7052c0d5bd9a071df0")
!277 = !{!278}
!278 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !276, file: !2, baseType: !9, size: 64, align: 64, offset: 64, flags: DIFlagPublic)
!279 = !DIDerivedType(tag: DW_TAG_member, name: "Param", scope: !273, file: !2, baseType: !280, size: 128, align: 64, extraData: i128 1)
!280 = !DICompositeType(tag: DW_TAG_structure_type, name: "Param", scope: !271, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !281, templateParams: !23, identifier: "2af83dd5878d38d22bbdb2895f5aa174")
!281 = !{!282}
!282 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !280, file: !2, baseType: !9, size: 64, align: 64, offset: 64, flags: DIFlagPublic)
!283 = !DIDerivedType(tag: DW_TAG_member, name: "Implied", scope: !273, file: !2, baseType: !284, size: 128, align: 64, extraData: i128 2)
!284 = !DICompositeType(tag: DW_TAG_structure_type, name: "Implied", scope: !271, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !23, identifier: "2c51204f3dd61f04a220a1ef80081768")
!285 = !DIDerivedType(tag: DW_TAG_member, scope: !271, file: !2, baseType: !191, size: 64, align: 64, flags: DIFlagArtificial)
!286 = !DIDerivedType(tag: DW_TAG_member, name: "width", scope: !264, file: !2, baseType: !271, size: 128, align: 64, offset: 128, flags: DIFlagPublic)
!287 = !DIDerivedType(tag: DW_TAG_member, name: "length", scope: !260, file: !2, baseType: !9, size: 64, align: 64, offset: 64)
!288 = !DIDerivedType(tag: DW_TAG_member, name: "Some", scope: !254, file: !2, baseType: !289, size: 128, align: 64)
!289 = !DICompositeType(tag: DW_TAG_structure_type, name: "Some", scope: !252, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !290, templateParams: !258, identifier: "c0ce6bbbc769fda6e1d63399d2844f93")
!290 = !{!291}
!291 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !289, file: !2, baseType: !260, size: 128, align: 64, flags: DIFlagPublic)
!292 = !DIDerivedType(tag: DW_TAG_member, scope: !252, file: !2, baseType: !191, size: 64, align: 64, flags: DIFlagArtificial)
!293 = !DIDerivedType(tag: DW_TAG_member, name: "args", scope: !238, file: !2, baseType: !294, size: 128, align: 64, offset: 128, flags: DIFlagPrivate)
!294 = !DICompositeType(tag: DW_TAG_structure_type, name: "&[core::fmt::rt::Argument]", file: !2, size: 128, align: 64, elements: !295, templateParams: !23, identifier: "cbf2a87147ba757171f66337af53028")
!295 = !{!296, !321}
!296 = !DIDerivedType(tag: DW_TAG_member, name: "data_ptr", scope: !294, file: !2, baseType: !297, size: 64, align: 64)
!297 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !298, size: 64, align: 64, dwarfAddressSpace: 0)
!298 = !DICompositeType(tag: DW_TAG_structure_type, name: "Argument", scope: !34, file: !2, size: 128, align: 64, flags: DIFlagPublic, elements: !299, templateParams: !23, identifier: "fd40be3ce111398c7cfc5b390b823fe8")
!299 = !{!300}
!300 = !DIDerivedType(tag: DW_TAG_member, name: "ty", scope: !298, file: !2, baseType: !301, size: 128, align: 64, flags: DIFlagPrivate)
!301 = !DICompositeType(tag: DW_TAG_structure_type, name: "ArgumentType", scope: !34, file: !2, size: 128, align: 64, flags: DIFlagPrivate, elements: !302, templateParams: !23, identifier: "46720f6713d5af00a0bd1cf3d345fb8f")
!302 = !{!303}
!303 = !DICompositeType(tag: DW_TAG_variant_part, scope: !301, file: !2, size: 128, align: 64, elements: !304, templateParams: !23, identifier: "c3f51eed59c30ea55cbab66e1b2d1726", discriminator: !320)
!304 = !{!305, !316}
!305 = !DIDerivedType(tag: DW_TAG_member, name: "Placeholder", scope: !303, file: !2, baseType: !306, size: 128, align: 64)
!306 = !DICompositeType(tag: DW_TAG_structure_type, name: "Placeholder", scope: !301, file: !2, size: 128, align: 64, flags: DIFlagPrivate, elements: !307, templateParams: !23, identifier: "4a6344bebc738360be953e966df40147")
!307 = !{!308, !312}
!308 = !DIDerivedType(tag: DW_TAG_member, name: "value", scope: !306, file: !2, baseType: !309, size: 64, align: 64, flags: DIFlagPrivate)
!309 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "&core::fmt::rt::{extern#0}::Opaque", baseType: !310, size: 64, align: 64, dwarfAddressSpace: 0)
!310 = !DICompositeType(tag: DW_TAG_structure_type, name: "Opaque", scope: !311, file: !2, align: 8, elements: !23, identifier: "8c7730c90efd023bfd7c068017e61ded")
!311 = !DINamespace(name: "{extern#0}", scope: !34)
!312 = !DIDerivedType(tag: DW_TAG_member, name: "formatter", scope: !306, file: !2, baseType: !313, size: 64, align: 64, offset: 64, flags: DIFlagPrivate)
!313 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "fn(&core::fmt::rt::{extern#0}::Opaque, &mut core::fmt::Formatter) -> core::result::Result<(), core::fmt::Error>", baseType: !314, size: 64, align: 64, dwarfAddressSpace: 0)
!314 = !DISubroutineType(types: !315)
!315 = !{!149, !309, !168}
!316 = !DIDerivedType(tag: DW_TAG_member, name: "Count", scope: !303, file: !2, baseType: !317, size: 128, align: 64, extraData: i128 0)
!317 = !DICompositeType(tag: DW_TAG_structure_type, name: "Count", scope: !301, file: !2, size: 128, align: 64, flags: DIFlagPrivate, elements: !318, templateParams: !23, identifier: "6affd3b48042584a3ec3f29f86443fa1")
!318 = !{!319}
!319 = !DIDerivedType(tag: DW_TAG_member, name: "__0", scope: !317, file: !2, baseType: !9, size: 64, align: 64, flags: DIFlagPrivate)
!320 = !DIDerivedType(tag: DW_TAG_member, scope: !301, file: !2, baseType: !191, size: 64, align: 64, offset: 64, flags: DIFlagArtificial)
!321 = !DIDerivedType(tag: DW_TAG_member, name: "length", scope: !294, file: !2, baseType: !9, size: 64, align: 64, offset: 64)
!322 = !DISubroutineType(types: !323)
!323 = !{!238, !241, !294}
!324 = !DISubprogram(name: "new_v1", linkageName: "_ZN4core3fmt9Arguments6new_v117hc7d70b2a7a10bb03E", scope: !238, file: !211, line: 339, type: !322, scopeLine: 339, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !23)
!325 = !{!326, !327}
!326 = !DILocalVariable(name: "pieces", arg: 1, scope: !237, file: !211, line: 339, type: !241)
!327 = !DILocalVariable(name: "args", arg: 2, scope: !237, file: !211, line: 339, type: !294)
!328 = !DILocation(line: 339, column: 19, scope: !237)
!329 = !DILocation(line: 339, column: 47, scope: !237)
!330 = !DILocation(line: 340, column: 12, scope: !237)
!331 = !DILocation(line: 340, column: 56, scope: !237)
!332 = !DILocation(line: 340, column: 41, scope: !237)
!333 = !DILocation(line: 341, column: 20, scope: !237)
!334 = !DILocalVariable(name: "pieces", arg: 1, scope: !335, file: !211, line: 329, type: !241)
!335 = distinct !DILexicalBlock(scope: !336, file: !211, line: 329, column: 5)
!336 = distinct !DISubprogram(name: "new_const", linkageName: "_ZN4core3fmt9Arguments9new_const17h03516e715c2b11c9E", scope: !238, file: !211, line: 329, type: !337, scopeLine: 329, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, declaration: !339, retainedNodes: !340)
!337 = !DISubroutineType(types: !338)
!338 = !{!238, !241}
!339 = !DISubprogram(name: "new_const", linkageName: "_ZN4core3fmt9Arguments9new_const17h03516e715c2b11c9E", scope: !238, file: !211, line: 329, type: !337, scopeLine: 329, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !23)
!340 = !{!334}
!341 = !DILocation(line: 329, column: 28, scope: !335, inlinedAt: !342)
!342 = !DILocation(line: 106, column: 38, scope: !343)
!343 = !DILexicalBlockFile(scope: !237, file: !344, discriminator: 0)
!344 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/panic.rs", directory: "", checksumkind: CSK_MD5, checksum: "6585507958cf42cd7ac7ae9875a25d92")
!345 = !DILocation(line: 333, column: 9, scope: !335, inlinedAt: !342)
!346 = !DILocation(line: 341, column: 13, scope: !237)
!347 = !DILocation(line: 343, column: 9, scope: !237)
!348 = !DILocation(line: 344, column: 6, scope: !237)
!349 = !DILocation(line: 340, column: 71, scope: !237)
!350 = distinct !DISubprogram(name: "call_once<std::rt::lang_start::{closure_env#0}<()>, ()>", linkageName: "_ZN4core3ops8function6FnOnce40call_once$u7b$$u7b$vtable.shim$u7d$$u7d$17ha807470326e2055bE", scope: !352, file: !351, line: 250, type: !355, scopeLine: 250, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !361, retainedNodes: !358)
!351 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/ops/function.rs", directory: "", checksumkind: CSK_MD5, checksum: "abc772494ea8033dad5cae2e40e54b10")
!352 = !DINamespace(name: "FnOnce", scope: !353)
!353 = !DINamespace(name: "function", scope: !354)
!354 = !DINamespace(name: "ops", scope: !36)
!355 = !DISubroutineType(types: !356)
!356 = !{!100, !357}
!357 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "*mut std::rt::lang_start::{closure_env#0}<()>", baseType: !14, size: 64, align: 64, dwarfAddressSpace: 0)
!358 = !{!359, !360}
!359 = !DILocalVariable(arg: 1, scope: !350, file: !351, line: 250, type: !357)
!360 = !DILocalVariable(arg: 2, scope: !350, file: !351, line: 250, type: !7)
!361 = !{!362, !363}
!362 = !DITemplateTypeParameter(name: "Self", type: !14)
!363 = !DITemplateTypeParameter(name: "Args", type: !7)
!364 = !DILocation(line: 250, column: 5, scope: !350)
!365 = distinct !DISubprogram(name: "call_once<std::rt::lang_start::{closure_env#0}<()>, ()>", linkageName: "_ZN4core3ops8function6FnOnce9call_once17h576cf1e5a88dab71E", scope: !352, file: !351, line: 250, type: !366, scopeLine: 250, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !361, retainedNodes: !368)
!366 = !DISubroutineType(types: !367)
!367 = !{!100, !14}
!368 = !{!369, !370}
!369 = !DILocalVariable(arg: 1, scope: !365, file: !351, line: 250, type: !14)
!370 = !DILocalVariable(arg: 2, scope: !365, file: !351, line: 250, type: !7)
!371 = !DILocation(line: 250, column: 5, scope: !365)
!372 = distinct !DISubprogram(name: "call_once<fn(), ()>", linkageName: "_ZN4core3ops8function6FnOnce9call_once17h9bca4dd66ad55774E", scope: !352, file: !351, line: 250, type: !48, scopeLine: 250, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !376, retainedNodes: !373)
!373 = !{!374, !375}
!374 = !DILocalVariable(arg: 1, scope: !372, file: !351, line: 250, type: !20)
!375 = !DILocalVariable(arg: 2, scope: !372, file: !351, line: 250, type: !7)
!376 = !{!377, !363}
!377 = !DITemplateTypeParameter(name: "Self", type: !20)
!378 = !DILocation(line: 250, column: 5, scope: !372)
!379 = distinct !DISubprogram(name: "drop_in_place<std::rt::lang_start::{closure_env#0}<()>>", linkageName: "_ZN4core3ptr85drop_in_place$LT$std..rt..lang_start$LT$$LP$$RP$$GT$..$u7b$$u7b$closure$u7d$$u7d$$GT$17h3bd5227b6af50977E", scope: !381, file: !380, line: 514, type: !382, scopeLine: 514, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !386, retainedNodes: !384)
!380 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/ptr/mod.rs", directory: "", checksumkind: CSK_MD5, checksum: "27e8e5f818674b264cf471331a16e438")
!381 = !DINamespace(name: "ptr", scope: !36)
!382 = !DISubroutineType(types: !383)
!383 = !{null, !357}
!384 = !{!385}
!385 = !DILocalVariable(arg: 1, scope: !379, file: !380, line: 514, type: !357)
!386 = !{!387}
!387 = !DITemplateTypeParameter(name: "T", type: !14)
!388 = !DILocation(line: 514, column: 1, scope: !379)
!389 = distinct !DISubprogram(name: "report", linkageName: "_ZN54_$LT$$LP$$RP$$u20$as$u20$std..process..Termination$GT$6report17h365417c523693d0cE", scope: !390, file: !107, line: 2411, type: !391, scopeLine: 2411, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, retainedNodes: !393)
!390 = !DINamespace(name: "{impl#57}", scope: !110)
!391 = !DISubroutineType(types: !392)
!392 = !{!109, !7}
!393 = !{!394, !395}
!394 = !DILocalVariable(name: "self", scope: !389, file: !107, line: 2411, type: !7, align: 1)
!395 = !DILocalVariable(arg: 1, scope: !389, file: !107, line: 2411, type: !7)
!396 = !DILocation(line: 2411, column: 15, scope: !389)
!397 = !DILocation(line: 2413, column: 6, scope: !389)
!398 = distinct !DISubprogram(name: "factorial", linkageName: "_ZN4main9factorial17h8e596bd882e49064E", scope: !400, file: !399, line: 1, type: !401, scopeLine: 1, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !23, retainedNodes: !403)
!399 = !DIFile(filename: "main.rs", directory: "/home/admin/Documents/codemetrics/software_metrics/run_metrics/rust_examples/src", checksumkind: CSK_MD5, checksum: "d3757bdf1d2abace7f84e09d2a6f561c")
!400 = !DINamespace(name: "main", scope: null)
!401 = !DISubroutineType(types: !402)
!402 = !{!167, !167}
!403 = !{!404}
!404 = !DILocalVariable(name: "n", arg: 1, scope: !398, file: !399, line: 1, type: !167)
!405 = !DILocation(line: 1, column: 14, scope: !398)
!406 = !DILocation(line: 2, column: 5, scope: !398)
!407 = !DILocation(line: 4, column: 28, scope: !398)
!408 = !DILocation(line: 3, column: 18, scope: !398)
!409 = !DILocation(line: 6, column: 2, scope: !398)
!410 = !DILocation(line: 4, column: 18, scope: !398)
!411 = !DILocation(line: 4, column: 14, scope: !398)
!412 = !DILocation(line: 4, column: 31, scope: !398)
!413 = distinct !DISubprogram(name: "main", linkageName: "_ZN4main4main17h0ac0b47279fbf2b6E", scope: !400, file: !399, line: 8, type: !21, scopeLine: 8, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition | DISPFlagMainSubprogram, unit: !30, templateParams: !23, retainedNodes: !414)
!414 = !{!415}
!415 = !DILocalVariable(name: "var1", scope: !416, file: !399, line: 9, type: !167, align: 16)
!416 = distinct !DILexicalBlock(scope: !413, file: !399, line: 9, column: 5)
!417 = !DILocation(line: 9, column: 9, scope: !416)
!418 = !DILocation(line: 9, column: 16, scope: !413)
!419 = !DILocalVariable(name: "x", arg: 1, scope: !420, file: !421, line: 112, type: !166)
!420 = distinct !DISubprogram(name: "new_display<u128>", linkageName: "_ZN4core3fmt2rt8Argument11new_display17h6a476e789c43298cE", scope: !298, file: !421, line: 112, type: !422, scopeLine: 112, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !425, declaration: !424, retainedNodes: !427)
!421 = !DIFile(filename: "/usr/src/debug/rust/rustc-1.79.0-src/library/core/src/fmt/rt.rs", directory: "", checksumkind: CSK_MD5, checksum: "97b307aeb2cfde091afce8909100596c")
!422 = !DISubroutineType(types: !423)
!423 = !{!298, !166}
!424 = !DISubprogram(name: "new_display<u128>", linkageName: "_ZN4core3fmt2rt8Argument11new_display17h6a476e789c43298cE", scope: !298, file: !421, line: 112, type: !422, scopeLine: 112, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !425)
!425 = !{!426}
!426 = !DITemplateTypeParameter(name: "T", type: !167)
!427 = !{!419}
!428 = !DILocation(line: 112, column: 40, scope: !420, inlinedAt: !429)
!429 = distinct !DILocation(line: 10, column: 5, scope: !416)
!430 = !DILocalVariable(name: "x", arg: 1, scope: !431, file: !421, line: 92, type: !166)
!431 = distinct !DILexicalBlock(scope: !432, file: !421, line: 92, column: 5)
!432 = distinct !DISubprogram(name: "new<u128>", linkageName: "_ZN4core3fmt2rt8Argument3new17h42933cd7ddd38902E", scope: !298, file: !421, line: 92, type: !433, scopeLine: 92, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !425, declaration: !436, retainedNodes: !437)
!433 = !DISubroutineType(types: !434)
!434 = !{!298, !166, !435}
!435 = !DIDerivedType(tag: DW_TAG_pointer_type, name: "fn(&u128, &mut core::fmt::Formatter) -> core::result::Result<(), core::fmt::Error>", baseType: !147, size: 64, align: 64, dwarfAddressSpace: 0)
!436 = !DISubprogram(name: "new<u128>", linkageName: "_ZN4core3fmt2rt8Argument3new17h42933cd7ddd38902E", scope: !298, file: !421, line: 92, type: !433, scopeLine: 92, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !425)
!437 = !{!430, !438}
!438 = !DILocalVariable(name: "f", arg: 2, scope: !431, file: !421, line: 92, type: !435)
!439 = !DILocation(line: 92, column: 19, scope: !431, inlinedAt: !440)
!440 = distinct !DILocation(line: 113, column: 9, scope: !420, inlinedAt: !429)
!441 = !DILocation(line: 113, column: 22, scope: !420, inlinedAt: !429)
!442 = !DILocation(line: 92, column: 29, scope: !431, inlinedAt: !440)
!443 = !DILocation(line: 103, column: 21, scope: !431, inlinedAt: !440)
!444 = !DILocation(line: 102, column: 13, scope: !431, inlinedAt: !440)
!445 = !DILocation(line: 10, column: 53, scope: !416)
!446 = !DILocation(line: 10, column: 43, scope: !416)
!447 = !DILocalVariable(name: "x", arg: 1, scope: !448, file: !421, line: 116, type: !166)
!448 = distinct !DISubprogram(name: "new_debug<u128>", linkageName: "_ZN4core3fmt2rt8Argument9new_debug17h1d25a08a2d8aa149E", scope: !298, file: !421, line: 116, type: !422, scopeLine: 116, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !425, declaration: !449, retainedNodes: !450)
!449 = !DISubprogram(name: "new_debug<u128>", linkageName: "_ZN4core3fmt2rt8Argument9new_debug17h1d25a08a2d8aa149E", scope: !298, file: !421, line: 116, type: !422, scopeLine: 116, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit, templateParams: !425)
!450 = !{!447}
!451 = !DILocation(line: 116, column: 36, scope: !448, inlinedAt: !452)
!452 = distinct !DILocation(line: 10, column: 5, scope: !416)
!453 = !DILocalVariable(name: "x", arg: 1, scope: !454, file: !421, line: 92, type: !166)
!454 = distinct !DILexicalBlock(scope: !455, file: !421, line: 92, column: 5)
!455 = distinct !DISubprogram(name: "new<u128>", linkageName: "_ZN4core3fmt2rt8Argument3new17h42933cd7ddd38902E", scope: !298, file: !421, line: 92, type: !433, scopeLine: 92, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !30, templateParams: !425, declaration: !436, retainedNodes: !456)
!456 = !{!453, !457}
!457 = !DILocalVariable(name: "f", arg: 2, scope: !454, file: !421, line: 92, type: !435)
!458 = !DILocation(line: 92, column: 19, scope: !454, inlinedAt: !459)
!459 = distinct !DILocation(line: 117, column: 9, scope: !448, inlinedAt: !452)
!460 = !DILocation(line: 117, column: 22, scope: !448, inlinedAt: !452)
!461 = !DILocation(line: 92, column: 29, scope: !454, inlinedAt: !459)
!462 = !DILocation(line: 103, column: 21, scope: !454, inlinedAt: !459)
!463 = !DILocation(line: 102, column: 13, scope: !454, inlinedAt: !459)
!464 = !DILocation(line: 10, column: 5, scope: !416)
!465 = !DILocation(line: 11, column: 2, scope: !413)
