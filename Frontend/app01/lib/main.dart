import 'package:app01/widgets/leftside.dart';
import 'package:app01/widgets/rightside.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';

import 'package:get/get.dart';
import 'package:window_manager/window_manager.dart';

import 'package:flutter/material.dart';

import 'controllers/menu_controller.dart';
import 'themes/Color_app.dart';



void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  await windowManager.ensureInitialized();
  const winsize = Size(1280, 720);
  WindowOptions windowOptions = const WindowOptions(
    size: Size(1280, 720),
    center: true,
    minimumSize: winsize,
    maximumSize: winsize,
  );
  windowManager.waitUntilReadyToShow(windowOptions, () async {
    await windowManager.setAsFrameless();
    await windowManager.setTitleBarStyle(TitleBarStyle.hidden);
    await windowManager.setResizable(false);
  });
  
  // doWhenWindowReady(() {
  //   final win = appWindow;
  //   const initialSize = Size(1280, 720); // ขนาดที่เล็กที่สุดที่สามารถย่อได้
  //   // win.maxSize = const Size(1280, 720); // ขนาดที่ใหญ่ที่สุดที่สามารถขยายได้
  //   win.minSize = initialSize;
  //   win.size = initialSize;
  //   win.maxSize = initialSize;
  //   win.alignment = Alignment.center;
  //   win.title = "Echo-Echo";
  //   win.show();
  // });
  Get.put(MenuController());
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: WindowBorder(
          color: AppColors.blackColor,
          width: 1,
          child: Row(
            children: const [LeftSide(), RightSide()],
          ),
        ),
      ),
    );
  }
}
