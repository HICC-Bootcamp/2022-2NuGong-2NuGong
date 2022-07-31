import React from 'react';
import { Text } from 'react-native';

const FontText = props => {
  return (
    <Text {...props} style={{ ...props.style, fontFamily: 'roboto' }}>
      {props.childern}
    </Text>
  );
};
export default FontText;
