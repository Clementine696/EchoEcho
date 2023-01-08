import 'package:flutter/material.dart';
import 'package:get/get.dart';

class MenuController extends GetxController {
  static MenuController instance = Get.find();
  var activeItem = 'microphonepageroute'.obs;
  var hoverItem = ''.obs;

  changeActiveItemTo(String itemName) {
    activeItem.value = itemName;
  }

  onHover(String itemName) {
    if (!isActive(itemName)) hoverItem.value = itemName;
  }

  isActive(String itemName) => activeItem.value == itemName;

  isHovering(String itemName) => hoverItem.value == itemName;

  Widget returnIconFor(String itemName) {
    switch (itemName) {
      case 'microphonepageroute':
        return _customIcon(Icons.mic, itemName);
      case 'audiopageroute':
        return _customIcon(Icons.volume_up, itemName);
      case 'soundpadpageroute':
        return _customIcon(Icons.play_circle_fill, itemName);
      case 'voicechangerpageroute':
        return _customIcon(Icons.change_history_rounded, itemName);
      default:
        return _customIcon(Icons.mic, itemName);
    }
  }

  Widget _customIcon(IconData icon,String itemName) {
    if(isActive(itemName)) return Icon(icon,color: Colors.black, size: 22,);

    return Icon(icon, color: isHovering(itemName) ? Colors.white : Colors.blueGrey,);
  }
}