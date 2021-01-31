import React, { Component } from 'react';

import InputBox from './inputBox.js'
import SubmitButton from './submitButton.js'

class TwitterPage extends Component {
    constructor(props) {
        super(props);


    }

  render() {
    return (
        <div>
            <h1> Twitter-Analyzer </h1>
            <InputBox/>
            <SubmitButton/>
        </div>
  );
  }
}


export default TwitterPage;