import 'dart:ui';

import 'package:flutter/material.dart';

import '../../themes/Color_app.dart';

class Dropdownspeaker extends StatefulWidget {
  const Dropdownspeaker({super.key});

  @override
  State<Dropdownspeaker> createState() => _DropdownspeakerState();
}

class _DropdownspeakerState extends State<Dropdownspeaker> {
  final items = ['Speaker 1', 'Speaker 2', 'Speaker 3'];
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

class Dropdowniconspeaker extends StatefulWidget {
  const Dropdowniconspeaker({super.key});

  @override
  State<Dropdowniconspeaker> createState() => _DropdowniconspeakerState();
}

class _DropdowniconspeakerState extends State<Dropdowniconspeaker> {
  @override
  Widget build(BuildContext context) {
    return Container(
        width: 380,
        child: Container(
          padding: EdgeInsets.only(left: 15),
          child: Row(
            children: [
              const Expanded(flex: 0, child: iconspeaker()),
              const Expanded(flex: 0, child: Dropdownspeaker())
            ],
          ),
        ));
  }
}

class iconspeaker extends StatefulWidget {
  const iconspeaker({super.key});

  @override
  State<iconspeaker> createState() => _iconspeakerState();
}

class _iconspeakerState extends State<iconspeaker> {
  bool click = true;
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          primary: Colors.transparent,
          elevation: 0,
          shadowColor: Colors.transparent.withOpacity(0),
          foregroundColor: AppColors.fdColor,
        ),
        onPressed: () {
          setState(() {
            click = !click;
          });
        },
        child: Icon(
          (click == false) ? Icons.volume_up : Icons.volume_off,
          size: 40,
          color: AppColors.whiteColor,
        ),
      ),
    );
  }
}
