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

        // Map<String,String> myMap = Map.from(snapshot.data)

        // String textOutputOrError = Chaquopy.executeCode("C:/Users/user/Desktop/EchoEcho/Backend/OnOff.py");

        // String code = 'a=10\nprint(a)';

        // Future<String> fileContains(String Output, String Error) async {
        //   var result = await Chaquopy.executeCode(code);
        //   return result["Output"];
        // }

        // Future myFutureAsVoid() {}


        Future fetchUserOrder(String Output, String Error) {
          String code = 'a=10\nprint(a)';
          return Chaquopy.executeCode(code);
        }
          

        var result = fetchUserOrder();
        debugPrint('Fetching user order..');
        

        
        // Future<bool> fileContains(String path, String needle) async {
        //   var haystack = await File(path).readAsString();
        //   return haystack.contains(needle);
        // }

        // String code = 'a=10/nprint(a)';
        // Chaquopy.executeCode(code);

        // Map map = new HashMap();
        // map.put(Chaquopy.executeCode(code));
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