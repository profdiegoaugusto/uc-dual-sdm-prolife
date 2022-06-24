import { useNavigation } from "@react-navigation/native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

import { AppStackParams } from "../routes/routes";

export function useAppNavigation() {
  const navigation = useNavigation<NativeStackScreenProps<AppStackParams>>();
  return navigation;
}
