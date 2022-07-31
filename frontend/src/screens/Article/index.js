import React, { useEffect, useState } from 'react';
import {
  Text,
  View,
  SafeAreaView,
  ScrollView,
  TouchableOpacity,
  Linking,
} from 'react-native';
import styled from 'styled-components/native';
import FontText from '../../components/FontText';

convertTag = {
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

const ArticleScreen = ({ route }) => {
  const [data, setData] = useState({});

  useEffect(() => {
    setData(route.params.data);
  }, []);

  return (
    <Wrapper>
      <SafeAreaView>
        <ScrollWrapper>
          <ArticleWrapper>
            <AritcleTag>[{convertTag[data.tag]}]</AritcleTag>
            <ArticleTitle>{data.title}</ArticleTitle>
            <TouchableOpacity
              onPress={() => {
                Linking.openURL(data.url);
              }}>
              <AritcleLink>[원문 보기]</AritcleLink>
            </TouchableOpacity>
            <ArticleDescription>{data.contents}</ArticleDescription>
          </ArticleWrapper>
        </ScrollWrapper>
      </SafeAreaView>
    </Wrapper>
  );
};

const Wrapper = styled.View`
  background-color: white;
`;

const SafeWrapper = styled.SafeAreaView``;

const ScrollWrapper = styled.ScrollView`
  height: 100%;
  padding: 25px;
`;

const ArticleWrapper = styled.View`
  margin-top: 30px;
  margin-bottom: 30px;
`;

const AritcleTag = styled.Text`
  font-weight: 900;
  font-size: 20px;
  color: rgba(3, 17, 144, 0.63);
`;

const ArticleTitle = styled.Text`
  font-weight: 700;
  font-size: 20px;
  margin-top: 10px;
  display: flex;
  align-items: center;

  color: #262626;
`;

const AritcleLink = styled.Text`
  font-weight: 700;
  font-size: 15px;
  text-decoration-line: underline;

  color: rgba(3, 17, 144, 0.63);
  margin-top: 40px;
`;

const ArticleDescription = styled.Text`
  font-weight: 500;
  font-size: 15px;
  margin-top: 10px;
  color: #646464;
  white-space: pre;
  word-break: keep-all;
`;

export default ArticleScreen;
