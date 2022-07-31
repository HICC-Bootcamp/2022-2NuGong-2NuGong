import React, { useEffect, useLayoutEffect, useState } from 'react';
import {
  Text,
  View,
  SafeAreaView,
  ScrollView,
  TouchableOpacity,
} from 'react-native';

import styled from 'styled-components/native';

import LogoImg from '../../assets/logo.svg';

import axios from 'axios';
import { API_URL } from '@env';
import { useIsFocused } from '@react-navigation/native';
import ArticleList from '../../components/ArticleList';

const SettingsScreen = ({ navigation }) => {
  const focus = useIsFocused();

  useEffect(() => {
    if (focus) {
    }
  }, [focus]);

  return (
    <Wrapper>
      <SafeWrapper edges={['right', 'left', 'top']}>
        <ScrollView>
          <LogoWrapper>
            <LogoImg />
          </LogoWrapper>

          <ContentContainer>
            <TouchableOpacity onPress={() => navigation.navigate('Login')}>
              <ContentWrapper>
                <ContentHeadText>로그인</ContentHeadText>
              </ContentWrapper>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => navigation.navigate('Register')}>
              <ContentWrapper>
                <ContentHeadText>회원가입</ContentHeadText>
              </ContentWrapper>
            </TouchableOpacity>
          </ContentContainer>
        </ScrollView>
      </SafeWrapper>
    </Wrapper>
  );
};

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

const SearchWrapper = styled.TouchableOpacity`
  position: absolute;
  right: 22px;
  top: 26px;
`;

const ContentContainer = styled.View`
  margin-top: 50px;
  margin-bottom: 70px;
`;

const ContentWrapper = styled.View`
  width: 335px;
  height: 45px;
  background-color: white;
  margin: auto;
  margin-top: 20px;
  border-radius: 10px;
  padding: 10px;
  padding-bottom: 10px;
`;

const ContentHeadText = styled.Text`
  font-weight: 700;
  font-size: 16px;
  color: rgba(3, 17, 144, 0.63);
  position: absolute;
  left: 20px;
  top: 13px;
`;

const ContentMoreButton = styled.TouchableOpacity`
  position: absolute;
  right: 20px;
  top: 23px;
`;

const ContentMoreText = styled.Text`
  font-weight: 700;
  font-size: 13px;
  /* identical to box height, or 77% */

  color: rgba(123, 126, 156, 0.63);
`;

const NoticeContainer = styled.View`
  margin-top: 40px;
`;

const NoticeWrapper = styled.TouchableOpacity`
  flex-direction: row;
  margin-bottom: 13px;
  width: 250px;
`;

const NoticeTagText = styled.Text`
  font-weight: 700;
  font-size: 13px;
  /* identical to box height, or 77% */

  color: #383838;
`;

const NoticeTitleText = styled.Text`
  font-weight: 500;
  font-size: 13px;
  /* or 77% */
  margin-left: 22px;
  color: #646464;
`;

export default SettingsScreen;
