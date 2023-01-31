import 'package:app01/themes/Color_app.dart';
import 'package:flutter/material.dart';

class MicrophonePage extends StatelessWidget {
  const MicrophonePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
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
                      shadowColor: AppColors.blackColor,
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.only(
                              topLeft: Radius.circular(25),
                              bottomLeft: Radius.circular(25)),
                          side: BorderSide(color: AppColors.blackColor)),
                      primary: AppColors.secDarkerColor),
                  onPressed: () {
                    debugPrint("Noise Suppression");
                  },
                  child: const Text.rich(TextSpan(children: <TextSpan>[
                    TextSpan(
                        text: "Noise Suppression\n",
                        style: TextStyle(
                            fontWeight: FontWeight.w600, fontSize: 30)),
                    TextSpan(
                        text:
                            "detecting the sound coming into the headset, and generating signals that are out-of-phase with the offending signals, cancelling them out.",
                        style: TextStyle(
                            fontWeight: FontWeight.w100,
                            fontSize: 20,
                            color: AppColors.grayDarkColor))
                  ]))),
            ),
            SizedBox(
              width: 389,
              height: 400,
              child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
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
                        text: "Echo Cancellation\n",
                        style: TextStyle(
                            fontWeight: FontWeight.w600, fontSize: 30)),
                    TextSpan(
                        text:
                            "methods used in telephony to improve voice quality by preventing echo from being created or removeing it after it is already present.",
                        style: TextStyle(
                            fontWeight: FontWeight.w100,
                            fontSize: 20,
                            color: AppColors.grayDarkColor))
                  ]))),
            )
          ],
        ),
        SizedBox(
            width: 778,
            height: 82,
            child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                    alignment: Alignment(-1, 0),
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(25)),
                    primary: AppColors.secDarkerColor),
                onPressed: () {
                  debugPrint("Test mic");
                },
                child: const Testmicicon())),
      ],
    );
  }
}

class Testmicicon extends StatefulWidget {
  const Testmicicon({super.key});

  @override
  State<Testmicicon> createState() => _TestmiciconState();
}

class _TestmiciconState extends State<Testmicicon> {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 380,
        child: Container(
          padding: EdgeInsets.only(left: 15),
          child: Row(
            children: [
              Text(
                "Test microphone",
                style: TextStyle(fontSize: 25, fontWeight: FontWeight.w100),
              ),
              //    Icon(
              //     Icons.square,
              //     color: AppColors.whiteColor,
              //    size: 40,
              //   ),
            ],
          ),
        ));
  }
}
