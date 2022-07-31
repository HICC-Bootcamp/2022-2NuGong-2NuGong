import React, { useState } from 'react';
import {
  Text,
  View,
  SafeAreaView,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';

import styled from 'styled-components/native';
import axios from 'axios';
import { API_URL } from '@env';
import LogoImg from '../../assets/logo.svg';
import BigLogoImg from '../../assets/biglogo.svg';

const RegisterScreen = ({ navigation }) => {
  const [idString, SetIdString] = useState('');
  const [pwString, SetPwString] = useState('');

  return (
    <Wrapper>
      <SafeWrapper edges={['right', 'left', 'top']}>
        <View>
          <LogoWrapper>
            <LogoImg />
          </LogoWrapper>
          <BigLogoWrapper>
            <BigLogoImg />
          </BigLogoWrapper>
          <LoginContainer>
            <InputWrapper
              placeholder="아이디"
              paddingHorizontal={20}
              autoCapitalize="none"
              onChangeText={text => SetIdString(text)}
            />
            <InputWrapper
              placeholder="비밀번호"
              paddingHorizontal={20}
              secureTextEntry={true}
              autoCapitalize="none"
              onChangeText={text => SetPwString(text)}
            />
            <LoginButton
              onPress={() => {
                console.log(idString);
                console.log(pwString);
                axios
                  .post(`${API_URL}/user/register/`, {
                    nickname: idString,
                    password: pwString,
                  })
                  .then(res => {
                    console.log(res.data);
                    Alert.alert('회원가입에 성공했습니다.', [
                      {
                        text: '확인',
                      },
                    ]);
                  })
                  .catch(err => {
                    console.log(err);
                    Alert.alert('회원가입에 실패했습니다.', [
                      {
                        text: '확인',
                      },
                    ]);
                  });
              }}>
              <LoginButtonText>회원가입</LoginButtonText>
            </LoginButton>
          </LoginContainer>
        </View>
      </SafeWrapper>
    </Wrapper>
  );
};

export default RegisterScreen;

const Wrapper = styled.View`
  background: rgba(3, 17, 144, 0.63);
`;

const SafeWrapper = styled.SafeAreaView`
  position: relative;
  height: 100%;
`;

const LogoWrapper = styled.View`
  position: absolute;
  left: 20px;
  top: 10px;
`;

const BigLogoWrapper = styled.View`
  margin: auto;
  margin-top: 110px;
  margin-bottom: 145px;
`;

const LoginContainer = styled.View`
  background-color: white;
  border-radius: 30px;
  height: 411px;
  padding: 20px;
`;

const InputWrapper = styled.TextInput`
  width: 337px;
  height: 42px;
  background: rgba(95, 100, 142, 0.1);
  border-radius: 25.5px;
  margin: 15px auto;
`;

const LoginButton = styled.TouchableOpacity`
  background-color: rgba(3, 17, 144, 0.6);
  border-radius: 25.5px;
  margin-top: 50px;
  width: 336.94px;
  height: 46.66px;
`;

const LoginButtonText = styled.Text`
  font-weight: 500;
  font-size: 14px;
  color: #fdfdff;
  margin: auto;
`;

const ResgisterText = styled.Text`
  font-weight: 500;
  font-size: 12px;
  margin: auto;
  margin-top: 70px;
  text-decoration-line: underline;

  color: rgba(157, 157, 157, 0.9);
`;
