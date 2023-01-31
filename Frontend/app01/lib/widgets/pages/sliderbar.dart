import 'package:flutter/material.dart';

import '../../themes/Color_app.dart';

class Sliderbar extends StatefulWidget {
  const Sliderbar({super.key});

  @override
  State<Sliderbar> createState() => _SliderbarState();
}

class _SliderbarState extends State<Sliderbar> {
  double _currentValue = 0;
  @override
  Widget build(BuildContext context) {
    return Column(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
      SizedBox(
        width: 370,
        child: Slider(
            value: _currentValue,
            min: 0,
            max: 100,
            divisions: 10,
            label: _currentValue.toString(),
            activeColor: AppColors.priLighterColor,
            inactiveColor: AppColors.grayLightColor,
            thumbColor: AppColors.priLighterColor,
            onChanged: ((value) {
              setState(() {
                _currentValue = value;
              });
            })),
      ),
    ]);
  }
}
