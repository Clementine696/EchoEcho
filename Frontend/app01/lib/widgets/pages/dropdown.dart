import 'dart:ui';

import 'package:flutter/material.dart';

import '../../themes/Color_app.dart';

class Dropdown extends StatefulWidget {
  const Dropdown({super.key});

  @override
  State<Dropdown> createState() => _DropdownState();
}

class _DropdownState extends State<Dropdown> {
  final items = ['Device 1', 'Device 2', 'Device 3'];
  final List<String> menuIcons = ['mic', 'speaker', 'play', 'magic2'];
  String? value;

  @override
  Widget build(BuildContext context) => Center(
        child: Container(
          width: 275,
          height: 44,
          padding: EdgeInsets.symmetric(horizontal: 10, vertical: 4),
          decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(4),
              border: Border.all(color: AppColors.fdDarkColor, width: 4),
              color: AppColors.fdDarkColor),
          child: DropdownButtonHideUnderline(
            child: DropdownButton<String>(
              value: value,
              isExpanded: true,
              iconSize: 25,
              borderRadius: BorderRadius.circular(4),
              dropdownColor: AppColors.grayLightColor,
              items: items.map(buildMenuItem).toList(),
              onChanged: (value) => setState(() => this.value = value),
              iconEnabledColor: AppColors.whiteColor,
              hint: Container(
                child: Text("Defalt",
                    style: TextStyle(
                        color: AppColors.whiteColor,
                        fontWeight: FontWeight.normal,
                        fontSize: 20)),
              ),
            ),
          ),
        ),
      );

  DropdownMenuItem<String> buildMenuItem(String item) => DropdownMenuItem(
        value: item,
        child: Text(
          item,
          style: const TextStyle(
              fontWeight: FontWeight.normal,
              fontSize: 20,
              color: AppColors.whiteColor),
        ),
      );
}

class Dropdownicon extends StatefulWidget {
  const Dropdownicon({super.key});

  @override
  State<Dropdownicon> createState() => _DropdowniconState();
}

class _DropdowniconState extends State<Dropdownicon> {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 380,
        child: Container(
          padding: EdgeInsets.only(left: 15),
          child: Row(
            children: [
              Icon(
                Icons.mic,
                color: AppColors.whiteColor,
                size: 40,
              ),
              const Expanded(child: Dropdown())
            ],
          ),
        ));
  }
}
