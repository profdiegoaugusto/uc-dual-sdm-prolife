import AsyncStorage from "@react-native-async-storage/async-storage";

function parse(value?: string | null) {
  return typeof value === "string" ? JSON.parse(value) : value;
}

async function getItem<T>(key: string): Promise<T> {
  return await AsyncStorage.getItem(key).then(parse);
}

function setItem<T>(key: string, value: T): void {
  AsyncStorage.setItem(key, JSON.stringify(value));
}

function removeItem(key: string): void {
  AsyncStorage.removeItem(key);
}

async function clearStorage() {
  await AsyncStorage.clear();
}
