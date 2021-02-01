import React, { Component } from "react";
import Form from 'react-bootstrap/Form'

export default class InputBox extends Component {
    constructor(props) {
        super(props);
        this.textInput = React.createRef();
    }

    render() {
        return (
            <div>
                <Form>
                    <Form.Group>
                        <Form.Control type="twitter_handle"
                                      placeholder="Enter username"
                                      size="lg"
                                      className="w-25"
                                      ref={this.textInput}
                                      onChange={() => this.props.onChange(this.textInput.current.value)}/>
                    </Form.Group>
                </Form>
            </div>
        );
    }
}
