import 'package:flutter/material.dart';

class AudioPage extends StatelessWidget {
  const AudioPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Container(
          width: 900,
          height: 160,
          color: Colors.red,
        ),
        Container(
          width: 900,
          height: 160,
          color: Colors.blue,
        ),
        Container(
          width: 900,
          height: 160,
          color: Colors.green,
        ),
        Container(
          width: 900,
          height: 160,
          color: Colors.yellow,
        ),
        // Container(
        //   child: ListView(
        //     // This next line does the trick.
        //     // Axis.vertical แนวตั้ง แต่พอเขียนแล้วสีหายเฉยเลย
        //     // scrollDirection: Axis.horizontal,
        //     children: <Widget>[
        //       Container(
        //         width: 160.0,
        //         color: Colors.red,
        //       ),
        //       Container(
        //         width: 160.0,
        //         color: Colors.blue,
        //       ),
        //       Container(
        //         width: 160.0,
        //         color: Colors.green,
        //       ),
        //       Container(
        //         width: 160.0,
        //         color: Colors.yellow,
        //       ),
        //       Container(
        //         width: 160.0,
        //         color: Colors.orange,
        //       ),
        //     ],
        //   ),
        // ),
      ],
    );
  }
}
