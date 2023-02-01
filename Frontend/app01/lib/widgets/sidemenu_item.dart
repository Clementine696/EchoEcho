import 'package:flutter/material.dart';
// import 'package:google_fonts/google_fonts.dart';

import '../themes/Color_app.dart';

class SidemenuItem extends StatefulWidget {
  const SidemenuItem({super.key});

  @override
  State<SidemenuItem> createState() => _SidemenuItemState();
}

class _SidemenuItemState extends State<SidemenuItem> {
  final List<String> menuItems = [
    'Microphone',
    'Audio',
    'SoundPad',
    'VoiceChanger'
  ];
  final List<String> menuIcons = ['mic', 'speaker', 'play', 'magic2'];

  int selectedMenuItem = 0;

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        SizedBox(
          width: double.infinity,
          child: Column(
            // mainAxisAlignment: MainAxisAlignment.spaceBetween,
            // mainAxisSize: MainAxisSize.max,
            children: <Widget>[
              Container(
                child: Expanded(
                  child: ListView.builder(
                    itemCount: menuItems.length,
                    itemBuilder: (context, index) => GestureDetector(
                        onTap: () {
                          setState(() {
                            selectedMenuItem = index;
                          });
                        },
                        child: MenuItem(
                          itemtext: menuItems[index],
                          itemicon: menuIcons[index],
                          selected: selectedMenuItem,
                          position: index,
                          menuselected: selectedMenuItem == index,
                        )
                      ),
                  ),
                ),
              ),
            ],
          ),
        ),
        // Container(
        //   transform: Matrix4.translationValues(380, 0, 1.0),
        //   width: double.infinity,
        //   height: double.infinity,
        // ),
      ],
    );
  }
}

class MenuItem extends StatelessWidget {
  final String itemtext;
  final String itemicon;
  final int selected;
  final int position;
  final bool menuselected;
  MenuItem(
      {required this.itemtext,
      required this.itemicon,
      required this.selected,
      required this.position,
      this.menuselected = false});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(top: 12),
      padding: const EdgeInsets.all(4),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: menuselected
              ? [AppColors.secLighterColor, AppColors.transparentColor]
              : [AppColors.transparentColor, AppColors.transparentColor],
          begin: Alignment.centerLeft,
          end: Alignment.centerRight,
        ),
      ),
      child: Row(
        children: <Widget>[
          Container(
            padding: const EdgeInsets.only(left: 32, bottom: 4),
            child: Image.asset("assets/$itemicon.png"),
          ),
          Container(
            padding: const EdgeInsets.only(left: 24, bottom: 10),
            child: Text(
              itemtext,
              style: const TextStyle(
                color: AppColors.whiteColor,
                fontSize: 32,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
