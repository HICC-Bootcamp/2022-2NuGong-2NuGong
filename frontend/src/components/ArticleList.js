import React, { useEffect, useState } from 'react';
import {
  Text,
  View,
  SafeAreaView,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import styled from 'styled-components/native';

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

const ArticleList = props => {
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

  useEffect(() => {
    setData(props.data);
  });
  return (
    <ContentContainer>
      {data.map((notice, index) => (
        <TouchableOpacity
          onPress={() => {
            props.navigation.navigate('Article', { data: notice });
          }}>
          <ContentWrapper key={index}>
            <ContentHeadWrapper>
              <ContentTagText>
                [
                {notice.tag === 'loading..'
                  ? notice.tag
                  : convertTag[notice.tag]}
                ]
              </ContentTagText>
              <ContentdepartmentText>
                {notice.department === 'loading..'
                  ? notice.department
                  : notice.department === 11
                  ? '컴퓨터공학과'
                  : '학교'}
              </ContentdepartmentText>
            </ContentHeadWrapper>
            <ContentTitleText>{notice.title}</ContentTitleText>
            <ContentcontentsText numberOfLines={5}>
              {notice.contents}
            </ContentcontentsText>
          </ContentWrapper>
        </TouchableOpacity>
      ))}
    </ContentContainer>
  );
};

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
`;

export default ArticleList;
