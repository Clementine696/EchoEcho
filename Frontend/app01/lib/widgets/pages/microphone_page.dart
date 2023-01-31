import 'package:app01/themes/Color_app.dart';
import 'package:flutter/material.dart';

class MicrophonePage extends StatelessWidget {
  const MicrophonePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: <Widget>[
        const Text(
          "Microphone Mode",
          style: TextStyle(
              color: AppColors.whiteColor,
              fontSize: 50,
              fontWeight: FontWeight.bold),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            SizedBox(
              width: 389,
              height: 400,
              child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.only(
                              topLeft: Radius.circular(25),
                              bottomLeft: Radius.circular(25)),
                          side: BorderSide(color: AppColors.blackColor)),
                      foregroundColor: Color.fromARGB(255, 3, 253, 240),
                      // backgroundColor: Color.fromARGB(47, 21, 227, 241),
                      primary: AppColors.secDarkerColor),
                  onPressed: () {
                    debugPrint("Noise Suppression");
                  },
                  child: const Text.rich(TextSpan(children: <TextSpan>[
                    TextSpan(
                        text: "Noise Suppression\n\n",
                        style: TextStyle(
                            color: Color.fromARGB(255, 255, 255, 255),
                            fontWeight: FontWeight.bold,
                            fontSize: 30)),
                    TextSpan(
                        text:
                            "detecting the sound coming into the headset, and generating signals that are out-of-phase with the offending signals, cancelling them out.",
                        style: TextStyle(
                            color: Color.fromARGB(255, 117, 115, 115),
                            fontWeight: FontWeight.normal,
                            fontSize: 20))
                  ]))),
            ),
            SizedBox(
                width: 389,
                height: 400,
                child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                        foregroundColor: Color.fromARGB(255, 3, 253, 240),
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.only(
                                topRight: Radius.circular(25),
                                bottomRight: Radius.circular(25))),
                        side: BorderSide(color: AppColors.blackColor),
                        primary: AppColors.secDarkerColor),
                    onPressed: () {
                      debugPrint("Echo Cancallation");
                    },
                    child: const Text.rich(TextSpan(children: <TextSpan>[
                      TextSpan(
                          text: "Echo Cancallation\n\n",
                          style: TextStyle(
                              color: Color.fromARGB(255, 255, 255, 255),
                              fontWeight: FontWeight.bold,
                              fontSize: 30)),
                      TextSpan(
                          text:
                              "methods used in telephony to improve voice quality by preventing echo from being created or removing it after it is already present.",
                          style: TextStyle(
                              color: Color.fromARGB(255, 117, 115, 115),
                              fontWeight: FontWeight.normal,
                              fontSize: 20))
                    ]))))
          ],
        ),
        SizedBox(
            width: 778,
            height: 82,
            child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(25)),
                    primary: AppColors.secDarkerColor),
                onPressed: () {
                  debugPrint("Test mic");
                },
                child: const Text(
                  "Test microphone",
                  style: TextStyle(fontSize: 30, fontWeight: FontWeight.normal),
                ))),
      ],
    );
  }
}
