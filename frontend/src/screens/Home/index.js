import React from 'react';
import {
  Button,
  View,
  Text,
  Image,
  ScrollView,
  TouchableOpacity,
  Pressable,
} from 'react-native';
import styled from 'styled-components/native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useState, useEffect } from 'react';
import axios from 'axios';

import { API_URL } from '@env';

import SearchImg from '../../assets/search/search.svg';
import LogoImg from '../../assets/logo.svg';
import { useIsFocused } from '@react-navigation/native';

const sectiondata = [
  { title: `학교 공지사항`, id: 1 },
  { title: `학과 공지사항`, id: 2 },
];

const convertTag = {
  1: '도서관',
  2: '고사',
  3: '전과',
  4: '장학',
  5: '동아리',
  6: '취업',
  7: '기숙사',
  8: '휴학·복학',
  9: '성적',
  10: '계절',
  11: '봉사',
  12: '프로그램',
  13: '기타',
  14: '행사/공모전',
};

const HomeScreen = ({ navigation }) => {
  const [noticeData0, setNoticeData0] = useState([
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

  const [noticeData11, setNoticeData11] = useState([
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
    await axios.get(`${API_URL}/search/?department=0`).then(res => {
      setNoticeData0(res.data);
    });
    await axios.get(`${API_URL}/search/?department=11`).then(res => {
      setNoticeData11(res.data);
    });
  };

  const focus = useIsFocused();

  useEffect(() => {
    if (focus) {
      GetData();
    }
  }, [focus]);

  return (
    <Wrapper>
      <SafeWrapper edges={['right', 'left', 'top']}>
        <ScrollView>
          <LogoWrapper>
            <LogoImg />
          </LogoWrapper>
          <SearchWrapper
            activeOpacity={0.8}
            onPress={() => navigation.navigate('Search')}>
            <SearchImg />
          </SearchWrapper>
          <ContentContainer>
            <ContentWrapper key={1}>
              <ContentHeadText>학과 공지사항</ContentHeadText>
              <ContentMoreButton
                onPress={() => {
                  navigation.navigate('Section', { id: data.id });
                }}>
                <ContentMoreText>더보기</ContentMoreText>
              </ContentMoreButton>
              <NoticeContainer>
                {noticeData11.slice(0, 6).map(notice => (
                  <NoticeWrapper
                    key={notice.id}
                    onPress={() => {
                      navigation.navigate('Article', { data: notice });
                    }}>
                    <NoticeTagText>{convertTag[notice.tag]}</NoticeTagText>
                    <NoticeTitleText numberOfLines={1}>
                      {notice.title}
                    </NoticeTitleText>
                  </NoticeWrapper>
                ))}
              </NoticeContainer>
            </ContentWrapper>
            <ContentWrapper key={2}>
              <ContentHeadText>학교 공지사항</ContentHeadText>
              <ContentMoreButton
                onPress={() => {
                  navigation.navigate('Section', { id: data.id });
                }}>
                <ContentMoreText>더보기</ContentMoreText>
              </ContentMoreButton>
              <NoticeContainer>
                {noticeData0.slice(0, 6).map(notice => (
                  <NoticeWrapper
                    key={notice.id}
                    onPress={() => {
                      navigation.navigate('Article', { data: notice });
                    }}>
                    <NoticeTagText>{convertTag[notice.tag]}</NoticeTagText>
                    <NoticeTitleText numberOfLines={1}>
                      {notice.title}
                    </NoticeTitleText>
                  </NoticeWrapper>
                ))}
              </NoticeContainer>
            </ContentWrapper>
          </ContentContainer>
        </ScrollView>
      </SafeWrapper>
    </Wrapper>
  );
};

export default HomeScreen;

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
  top: 10px;
`;

const ContentContainer = styled.View`
  margin-top: 50px;
  margin-bottom: 70px;
`;

const ContentWrapper = styled.View`
  width: 335px;

  background-color: white;
  margin: auto;
  margin-top: 20px;
  border-radius: 10px;
  padding: 20px;
  padding-bottom: 10px;
`;

const ContentHeadText = styled.Text`
  font-weight: 700;
  font-size: 16px;
  color: rgba(3, 17, 144, 0.63);
  position: absolute;
  left: 20px;
  top: 20px;
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
