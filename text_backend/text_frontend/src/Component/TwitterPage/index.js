import React, { Component } from 'react';

import InputBox from './inputBox.js';
import SubmitButton from './submitButton.js';
import StatBox from '../statBox.js';

import { get_headers } from '../sharedAPIs.js'
import { get_recent_tweets, get_from_username, post_create_text, get_text_analyzer} from './api.js'

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

    update_data(new_data) {
        this.setState({data: {
                                text_objects: [new_data]
        }});
    }

    handle_second_response(response) {
        if(response.status === 201){
            get_text_analyzer(response.data.id)
                .then(next_response => this.update_data(next_response.data.report));
        } else {
            console.log("An error occurred with the following response:");
            console.log(response);
        }

    }

    handle_response(response) {
        if(response.status === 208){
            get_text_analyzer(response.data.existing_id)
            .then(next_response => this.update_data(next_response.data.report));
        } else if(response.status === 200) {
            post_create_text(response.data)
                .then(response => this.handle_second_response(response))
                .catch(error => console.log(error))
        }
    }

    submit_username() {

        get_from_username(this.state.username)
            .then(response => this.handle_response(response))
            .catch( error => console.log(error));

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