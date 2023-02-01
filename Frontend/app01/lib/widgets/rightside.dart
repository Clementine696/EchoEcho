
import 'package:app01/widgets/right_body_page.dart';

import 'package:app01/widgets/windowbuttons.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';

import 'package:flutter/material.dart';

import '../themes/Color_app.dart';

class RightSide extends StatelessWidget {
  const RightSide({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [AppColors.fdLighterColor, AppColors.fdLighColor],
              stops: [0.0, 1.0]),
        ),
        child: Column(children: [
          WindowTitleBarBox(
            child: Row(
              children: [Expanded(child: MoveWindow()), const WindowButtons()],
            ),
          ),

          Expanded(child: RightBodyPage()),

        ]),
      ),
    );
  }
}
