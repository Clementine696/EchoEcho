import 'package:app01/widgets/pages/dropandslider.dart';
import 'package:app01/widgets/sidemenu_item.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';

import 'package:flutter/material.dart';

import '../themes/Color_app.dart';

class LeftSide extends StatefulWidget {
  const LeftSide({super.key});

  @override
  State<LeftSide> createState() => _LeftSideState();
}

class _LeftSideState extends State<LeftSide> {
  int _CurrentedPage = 0;
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 380,
      child: Container(
          color: AppColors.fdColor,
          child: Column(
            children: [
              WindowTitleBarBox(child: MoveWindow()),
              const Expanded(child: SidemenuItem()),
              const Expanded(child: DropandSlider()),
              //const Expanded(child: Sliderbar())
            ],
          )),
    );
  }
}
// class SideMenu extends StatefulWidget {
//   const SideMenu({super.key});

//   @override
//   State<SideMenu> createState() => _SideMenuState();
// }

// class _SideMenuState extends State<SideMenu> {
//   int currentPage = 0;
//   List<Widget> pages = [
//     Microphone(),
//     Audio(),
//     Soundpad(),
//     VoiceChanger(SideMenu)
//   ];
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       bottomNavigationBar: NavigationBar(
//         destinations: const [
//           NavigationRailDestination(icon: Icon(Icons.mic_none), label: 'Microphone'),
//           NavigationRailDestination(icon: Icon(Icons.volume_up_rounded), label: 'Audio'),
//           NavigationRailDestination(icon: Icon(Icons.play_circle_fill), label: 'Soundpad'),
//           NavigationRailDestination(icon: Icon(Icons.music_note_sharp), label: 'VoiceChanger'),
//         ],
//         onDestinationSelected: (int index) {
//           setState(() {
//             currentPage = index;
//           });
//         },
//         selectedIndex: currentPage,
//       ),

//     );
//   }
// }