import React from "react";
import { View, Text } from "react-native";
import { getStatusBarHeight } from "react-native-iphone-x-helper";

import { Container, Title } from "./styles";

const Home = () => (
  <Container>
    <Title>Hello Mobile World!</Title>
  </Container>
);

export { Home };
