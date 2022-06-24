import { StatusBar } from "expo-status-bar";
import { SafeAreaProvider } from "react-native-safe-area-context";
import {
  useFonts,
  Montserrat_400Regular,
  Montserrat_500Medium,
  Montserrat_700Bold,
} from "@expo-google-fonts/montserrat";
import AppLoading from "expo-app-loading";
import { ThemeProvider } from "styled-components";

import theme from "./src/global/theme";

import { Routes } from "./src/routes";

export default function App() {
  const [fontsLoaded] = useFonts({
    Montserrat_400Regular,
    Montserrat_500Medium,
    Montserrat_700Bold,
  });

  if (!fontsLoaded) {
    return <AppLoading />;
  }

  return (
    <SafeAreaProvider>
      <ThemeProvider theme={theme}>
        <StatusBar style="light" backgroundColor="#312e38" />
        <Routes />
      </ThemeProvider>
    </SafeAreaProvider>
  );
}
