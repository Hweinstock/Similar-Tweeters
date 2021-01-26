import React, { Component } from "react";

import axios from "axios";

export default class Message extends Component {
  constructor(props) {
    super(props);
    this.state = {
      msg:"",
    };
    this.loadMsg = this.loadMsg.bind(this);
  }


componentWillMount() {
  this.loadMsg();
}

async loadMsg()
{
  const promise = await axios.get("http://localhost:8000/api/test");
  const status = promise.status;
  if(status===200)
  {
    const data = promise.data.data;
    this.setState({msg:data});
  }
}

render() {
    console.log(this.state.msg);
  return(
    <div>
      <h1> Message </h1>
      <h4> {this.state.msg} </h4>
    </div>
  )
}
}
