import React, { createRef, useEffect, useState } from 'react';
import {
  View,
  Text,
  SafeAreaView,
  Image,
  ScrollView,
  TouchableOpacity,
  TextInput,
} from 'react-native';
import styled from 'styled-components/native';
import { SearchBar } from 'react-native-elements';
import axios from 'axios';
import { API_URL } from '@env';

import ArticleList from '../../components/ArticleList';

import ColorSearchImg from '../../assets/search/colorsearch.svg';
import BigSearchImg from '../../assets/search/bigsearch.svg';

const HomeScreen = ({ navigation }) => {
  const [isSearch, setIsSearch] = useState(false);
  const [searchText, setSearchText] = useState('');
  const [data, setData] = useState();

  const GetData = async keyword => {
    await axios
      .get(`${API_URL}/search?query=${keyword}`)
      .then(res => {
        setData(res.data);
      })
      .catch(err => {
        console.log(`${API_URL}/search?query=${keyword}`);
      });
  };

  useEffect(() => {
    setSearchText('');
  }, []);

  return (
    <Wrapper>
      <SafeAreaView style={{ position: 'relative', height: '100%' }}>
        <SearchBarContainer>
          <SearchBarWrapper
            value={searchText}
            onChangeText={text => {
              setSearchText(text);
            }}
            onSubmitEditing={() => GetData(searchText)}
            placeholder="검색어를 입력하세요"
            paddingHorizontal={30}>
            <ColorSearchWrapper>
              <ColorSearchImg />
            </ColorSearchWrapper>
          </SearchBarWrapper>
          <CancelButton activeOpacity={0.8} onPress={() => navigation.goBack()}>
            <CancelButtonText>취소</CancelButtonText>
          </CancelButton>
        </SearchBarContainer>
        {data && <ArticleList data={data} navigation={navigation} />}
        {!data && (
          <CenterWrapper>
            <BigSearchImg />
          </CenterWrapper>
        )}
      </SafeAreaView>
    </Wrapper>
  );
};

export default HomeScreen;

const Wrapper = styled.View`
  background: rgba(3, 17, 144, 0.63);
`;

const SearchBarContainer = styled.View`
  margin: 10px auto;
  width: 335px;
  flex-direction: row;
`;

const SearchBarWrapper = styled.TextInput`
  width: 290px;
  height: 33px;
  border-radius: 10px;
  background-color: white;
  position: relative;
`;

const CancelButton = styled.TouchableOpacity`
  margin: auto;
  margin-right: 0px;
`;

const CancelButtonText = styled.Text`
  margin: auto;
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  color: #ffffff;
`;

const ColorSearchWrapper = styled.View`
  position: absolute;
  top: 7px;
  left: 10px;
`;

const CenterWrapper = styled.View`
  margin: auto;
  margin-top: 200px;
`;
