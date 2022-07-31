import React from 'react';
import styled from 'styled-components/native';
import Icon from 'react-native-vector-icons/Ionicons';
Icon.loadFont();

const Pressable = styled.Pressable``;
const IconContainer = styled.View`
  opacity: ${({ pressed }) => (pressed ? 0.55 : 1)};
`;

const HeaderLeftGoBack = navigation => {
  return (
    <Pressable onPress={() => navigation.goBack()} hitSlop={8}>
      {({ pressed }) => (
        <IconContainer pressed={pressed}>
          <Icon size={30} name={'chevron-back'} color={'rgba(0,0,0,0.9)'} />
        </IconContainer>
      )}
    </Pressable>
  );
};

export default HeaderLeftGoBack;
