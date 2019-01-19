import React, { Component } from 'react';

import Msg from './components/Msg';

import './App.css';
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading:0,
      isLogined:false,
      id: '',
      password: '',
      loaded: 0,
      hashed: "",
      contents: [],
      toggle: {'홍보':true,'학사':true,'행정':true,'기타':true},
    };
    this.handleId=this.handleId.bind(this)
    this.handlePassword=this.handlePassword.bind(this)
    this.handleLogin=this.handleLogin.bind(this)
    this.handleToggle=this.handleToggle.bind(this)
  }
  componentDidMount(){
    this.setState({
      loding:1
    })
    fetch("http://localhost:1234")
      .then(res=>{
        return res.json();
      })
      .then(json=>{
        console.log(json)
        this.setState({
          contents: json,
          loding:0
        })
      })
  }

  handleId(e) {
    this.setState({ id: e.target.value });
  }

  handlePassword(e) {
    this.setState({ password: e.target.value });
  }

  handleLogin(){
    this.setState({
      loding:1
    })
    fetch("http://localhost:1234/login/?id="+this.state.id+"&password="+this.state.password)
      .then(res=>{
        return res.json();
      })
      .then(json=>{
        let login = true;
        if (json[0]['MESSAGE']==="로그인에 실패하셨습니다!!"){
          login=false
        }
        this.setState({
          contents: json,
          isLogined:login,
          loding:0
        })
    })
  }

  handleToggle(e) {
    let toggle = this.state.toggle
    toggle[e.target.innerText] = !toggle[e.target.innerText]
    this.setState({
      toggle: toggle
    })
  }

  render() {
    return (
      <div className="App">
      {this.state.isLogined===false?
        <div className="login">
          <input type="text" onChange={this.handleId}/>
          <input type="password" onChange={this.handlePassword}/>
          <span className="login-btn" onClick={this.handleLogin}>login</span>
        </div>:""}
        <div className="toggle">
          {this.state.loding===1?<div className="loading" />:<><span className="toggle-btn" onClick={this.handleToggle}>홍보</span>
          <span className="toggle-btn" onClick={this.handleToggle}>학사</span>
          <span className="toggle-btn" onClick={this.handleToggle}>행정</span>
          <span className="toggle-btn" onClick={this.handleToggle}>기타</span></>}

        </div>
        {this.state.contents.map((content,i) => {
          return (this.state.toggle[content['UPMU_GB_NM']]===true?<Msg when={content['SEND_DTTM']} p_num={content['SENDER_HP_NO']} id={content['ID']} filter={content['UPMU_GB_NM']} msg={content['MESSAGE']} key={i}/>:"")})}
      </div>
    );
  }
}


export default App;
