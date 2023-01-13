import 'package:bitsdojo_window/bitsdojo_window.dart';

import 'package:flutter/material.dart';

import '../themes/Color_app.dart';

final buttonColors = WindowButtonColors(
    iconNormal: const Color(0xFF805306),
    mouseOver: AppColors.secColor,
    mouseDown: AppColors.fdLighColor,
    iconMouseOver: const Color(0xFF805306),
    iconMouseDown: AppColors.whiteColor);

final closeButtonColors = WindowButtonColors(
    mouseOver: const Color(0xFFD32F2F),
    mouseDown: const Color(0xFFB71C1C),
    iconNormal: const Color(0xFF805306),
    iconMouseOver: AppColors.whiteColor);

class WindowButtons extends StatefulWidget {
  const WindowButtons({Key? key}) : super(key: key);

  @override
  _WindowButtonsState createState() => _WindowButtonsState();
}

class _WindowButtonsState extends State<WindowButtons> {
  void maximizeOrRestore() {
    setState(() {
      appWindow.maximizeOrRestore();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        MinimizeWindowButton(colors: buttonColors),
        CloseWindowButton(colors: closeButtonColors),
      ],
    );
  }
}

// class WindowButtons extends StatelessWidget {
//   const WindowButtons({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return Row(
//       children: [
//         MinimizeWindowButton(colors: buttonColors),
//         MaximizeWindowButton(colors: buttonColors),
//         CloseWindowButton(colors: closeButtonColors),
//       ],
//     );
//   }
// }
