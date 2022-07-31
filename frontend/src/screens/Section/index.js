import React, { useEffect, useLayoutEffect, useState } from 'react';
import {
  Text,
  View,
  SafeAreaView,
  ScrollView,
  TouchableOpacity,
} from 'react-native';

import ArticleList from '../../components/ArticleList';

import styled from 'styled-components/native';

import LogoImg from '../../assets/logo.svg';

import axios from 'axios';
import { API_URL } from '@env';

const FeedScreen = ({ navigation }) => {
  const [data, setData] = useState([
    {
      tag: 'loading..',
      title: 'loading..',
      contents: '\nloading..\n\n\n',
      department: 'loading..',
    },
    {
      tag: 'loading..',
      title: 'loading..',
      contents: '\nloading..\n\n\n',
      department: 'loading..',
    },
    {
      tag: 'loading..',
      title: 'loading..',
      contents: '\nloading..\n\n\n',
      department: 'loading..',
    },
    {
      tag: 'loading..',
      title: 'loading..',
      contents: '\nloading..\n\n\n',
      department: 'loading..',
    },
    {
      tag: 'loading..',
      title: 'loading..',
      contents: '\nloading..\n\n\n',
      department: 'loading..',
    },
    {
      tag: 'loading..',
      title: 'loading..',
      contents: '\nloading..\n\n\n',
      department: 'loading..',
    },
  ]);

  const GetData = async () => {
    await axios.get(`${API_URL}/notice`).then(res => {
      setData(res.data);
    });
  };

  useEffect(() => {
    GetData();
  }, []);

  return (
    <Wrapper>
      <SafeWrapper edges={['right', 'left', 'top']}>
        <ArticleList data={data} navigation={navigation} />
      </SafeWrapper>
    </Wrapper>
  );
};

const Wrapper = styled.View`
  background-color: white;
`;

const SafeWrapper = styled.SafeAreaView`
  height: 100%;
  position: relative;
`;

const HeaderWrapper = styled.View`
  position: relative;
  height: 40px;
`;

const LogoWrapper = styled.View`
  position: absolute;
  left: 20px;
  top: 10px;
`;

const ContentContainer = styled.ScrollView`
  background-color: white;
  padding: 22px;
`;

const ContentWrapper = styled.View`
  position: relative;
  border-bottom-color: rgba(3, 17, 144, 0.63);
  border-bottom-width: 1px;
  width: 100%;
  padding-bottom: 15px;
  margin-bottom: 20px;
`;

const ContentHeadWrapper = styled.View`
  height: 25px;
  flex-direction: row;
  width: 100%;
`;

const ContentTagText = styled.Text`
  font-size: 13px;
  font-weight: 700;
  color: rgba(3, 17, 144, 0.63);
`;

const ContentdepartmentText = styled.Text`
  font-size: 10px;
  color: #9b9b9b;
  margin: auto;
  margin-right: 0;
`;

const ContentTitleText = styled.Text`
  font-size: 13px;
  color: #262626;
  font-weight: 700;
  margin-bottom: 8px;
`;

const ContentcontentsText = styled.Text`
  color: #646464;
  font-weight: 500;
  font-size: 13px;
  white-space: pre-line;
`;

export default FeedScreen;
