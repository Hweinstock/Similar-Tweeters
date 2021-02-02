import React, { Component } from 'react';

import InputBox from './inputBox.js';
import SubmitButton from './submitButton.js';
import StatBox from '../statBox.js';

import { get_headers } from '../sharedAPIs.js'
import { get_recent_tweets } from './api.js'

class TwitterPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            username: "",
            data: undefined,
        };

        this.update_username = this.update_username.bind(this);
        this.submit_username = this.submit_username.bind(this);

    }

    update_username(username) {
        this.setState({username: username});
    }

    submit_username() {
        get_recent_tweets(this.state.username)
            .then(response => this.setState({data: {
                    text_objects: [response.data.report],
                    text: response.data.tweets,
                }}))
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <h1> Twitter-Analyzer </h1>
                <InputBox onChange={this.update_username}/>
                <SubmitButton onClick={this.submit_username}/>
                <StatBox get_headers={get_headers}
                         data={this.state.data}
                />
            </div>
        );
    }
}


export default TwitterPage;