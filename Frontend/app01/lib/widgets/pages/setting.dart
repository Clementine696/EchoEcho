import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:app01/themes/Color_app.dart';

class Setting extends StatefulWidget {
  const Setting({super.key});

  @override
  State<Setting> createState() => _SettingState();
}

class _SettingState extends State<Setting> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: TextButton.icon(
        onPressed: () {
          print("Setting");
        },
        icon: Icon(
          Icons.settings,
          color: AppColors.whiteColor,
          size: 40,
        ),
        label: Text(
          "Setting",
          style: TextStyle(
              fontSize: 32,
              fontWeight: FontWeight.normal,
              color: AppColors.whiteColor),
        ),
      ),
    );
  }
}
