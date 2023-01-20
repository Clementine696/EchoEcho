import 'package:auto_route/auto_route.dart';
import 'package:app01/widgets/Pages/microphone_page.dart';
import 'package:app01/main.dart';
// import 'package:auto_route/empty_router_widgets.dart';

// @MaterialAutoRouter(
//   replaceInRouteName: 'Page, Route',
//   routes: [
//     AutoRoute(path: '/', page: MicrophonePage, children: [
//       AutoRoute(
//         path: 'mic',
//         name: 'MicRoute',
//         // page: EmptyRouterPage,
//         children: [
//           AutoRoute(
//             path: '',
//             // page: MicrophonePage,
//           ),
//           AutoRoute(
//             path: ':micId',
//             // page: SingleMicPage,
//           ),
//         ],
//       ),
//       AutoRoute(
//         path: 'audio',
//         name: 'AudioRoute',
//         // page: EmptyRouterPage,
//         children: [
//           AutoRoute(
//             path: '',
//             // page: UsersPage,
//           ),
//           AutoRoute(
//             path: ':userId',
//             // page: UserprofilePage,
//           ),
//         ],
//       ),
//       AutoRoute(
//         path: 'soundpad',
//         name: 'SoundpadRoute',
//         // page: EmptyRouterPage,
//         children: [
//           AutoRoute(
//             path: "",
//             // page: SoundpadPage,
//           ),
//           AutoRoute(
//             path: ":soundpadId",
//             // page:  SingleSoundpadPage,
//           ),
//         ],
//       ),
//       AutoRoute(
//           path: 'Voicechanger',
//           name: 'VoicechangerRoute',
//           // page: EmptyRouterPage,
//           children: [
//             AutoRoute(
//               path: '',
//               // page: VoicechangerPage,
//             ),
//             AutoRoute(
//               path: ':voicechangerId',
//               // page: SingleVoicechangerPage,
//             ),
//           ])
//     ]),
//   ],
// )
// class $AppRoute {}

//SinglePostPagesRoute

class RouteGenerator {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    final args = settings.arguments;

    switch (settings.name) {

    }
  }
}