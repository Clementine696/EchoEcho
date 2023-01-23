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
        
        //TODO:

        Map<String,String> myMap = Map.from( snapshot.data )

        String textOutputOrError = Chaquopy.executeCode("C:/Users/user/Desktop/EchoEcho/Backend/OnOff.py");
        // debugPrint(textOutputOrError);

        // builder: (Chaquopy.executeCode("C:/Users/user/Desktop/EchoEcho/Backend/OnOff.py");, AsyncSnapshot<Map<String,String>> snapshot) {
        //   switch( snapshot.connectionState){
        //     case ConnectionState.none:
        //       return Text("there is no connection");
        // try {
        //   Chaquopy.executeCode("C:/Users/user/Desktop/EchoEcho/Backend/OnOff.py");
        // }
        // on Exception catch(e) {
        //   debugPrint('error caught: $e');
        // }
      },
      child: const Text('Test Microphone'),
    ),
      ],
    );
  }
}