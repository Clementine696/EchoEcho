import 'package:flutter/material.dart';


import 'menu_item.dart';

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
                        // Navigator.of(context).push(MaterialPageRoute(
                        //     builder: (context) =>
                        //         Scaffold(body: Text('microphone page'))));
                      },
                      child: MenuItems(
                        itemtext: menuItems[index],
                        itemicon: menuIcons[index],
                        selected: selectedMenuItem,
                        position: index,
                        menuselected: selectedMenuItem == index,
                      ),
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
