import 'package:app01/widgets/pages/dropdown.dart';
import 'package:bitsdojo_window/bitsdojo_window.dart';
import 'package:app01/widgets/pages/Sliderbar.dart';
import 'package:app01/widgets/pages/setting.dart';

import 'package:flutter/material.dart';

import '../../themes/Color_app.dart';
import 'dropdown_speaker.dart';

class DropandSlider extends StatefulWidget {
  const DropandSlider({super.key});

  @override
  State<DropandSlider> createState() => _DropandSliderState();
}

class _DropandSliderState extends State<DropandSlider> {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 380,
        child: Container(
          //  margin: EdgeInsets.only(bottom: 90),
          child: Column(
            children: const [
              Expanded(child: Dropdownicon()),
              Expanded(child: Sliderbar()),
              Expanded(child: Dropdowniconspeaker()),
              Expanded(child: Sliderbar()),
              Expanded(child: Setting())
            ],
          ),
        ));
  }
}
