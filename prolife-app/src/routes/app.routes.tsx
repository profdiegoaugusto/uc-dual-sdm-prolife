import React from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import { Home } from "../screens/Home";

const { Navigator, Screen } = createNativeStackNavigator();

function AppRoutes() {
  return (
    <Navigator
      screenOptions={{
        headerShown: false,
      }}
    >
      <Screen name="Home" component={Home} />
    </Navigator>
  );
}

export { AppRoutes };
