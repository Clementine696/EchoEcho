import 'package:bitsdojo_window/bitsdojo_window.dart';

import 'package:flutter/material.dart';

import '../themes/Color_app.dart';

class LeftSide extends StatelessWidget {
  const LeftSide({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 380,
        child: Container(
            color: AppColors.fdColor,
            child: Column(
              children: [
                WindowTitleBarBox(child: MoveWindow()),
                Expanded(child: Container())
              ],
            )));
  }
}
