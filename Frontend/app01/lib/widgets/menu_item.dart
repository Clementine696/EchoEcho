import 'package:flutter/material.dart';

import '../themes/Color_app.dart';

class MenuItems extends StatelessWidget {
  final String itemtext;
  final String itemicon;
  final int selected;
  final int position;
  final bool menuselected;
  const MenuItems(
      {super.key, required this.itemtext,
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
