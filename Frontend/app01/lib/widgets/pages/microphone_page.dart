import 'package:flutter/material.dart';

import '../../themes/Color_app.dart';

import 'package:chaquopy/chaquopy.dart';

class MicrophonePage extends StatelessWidget {
  const MicrophonePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
    const Text(
      "Microphone",
      style: TextStyle(color: AppColors.whiteColor, fontSize: 20),
    ),
    ElevatedButton(
      onPressed: () {
        debugPrint('Test Mic');

        Python.start();
        Python.run("C:/Users/user/Desktop/EchoEcho/Backend/OnOff.py");

      },
      child: const Text('Test Microphone'),
    ),
      ],
    );
  }
}