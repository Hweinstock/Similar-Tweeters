import React, { Component } from 'react';

import InputBox from './inputBox.js'
import SubmitButton from './submitButton.js'
import { get_recent_tweets } from './api.js'

class TwitterPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            username: ""
        };

        this.update_username = this.update_username.bind(this);
        this.submit_username = this.submit_username.bind(this);

    }

    update_username(username) {
        this.setState({username: username});
    }

    submit_username() {
        get_recent_tweets(this.state.username)
            .then(response => console.log(response))
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <h1> Twitter-Analyzer </h1>
                <InputBox onChange={this.update_username}/>
                <SubmitButton onClick={this.submit_username}/>
            </div>
        );
    }
}


export default TwitterPage;