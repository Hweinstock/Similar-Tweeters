import React, { Component } from "react";
// import Table from '@material-ui/core/Table';
// import TableBody from '@material-ui/core/TableBody';
// import TableCell from '@material-ui/core/TableCell';
// import TableContainer from '@material-ui/core/TableContainer';
// import TableHead from '@material-ui/core/TableHead';
// import TableRow from '@material-ui/core/TableRow';
import Table from 'react-bootstrap/Table'
// import Paper from '@material-ui/core/Paper';

import statBoxStyle from './shared_styling/statBox.module.css';


const column_header_mappings = {
    "top_words": "Keywords",
    "avg_word_length": "Average Word Length",
    "avg_sentence_length": "Average Sentence Length",
    "punctuation_percentages": "Punctuation Usage",
    "top_sentence_lengths": "Common Sentence Lengths",

};
export default class StatBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            headers: []
        };

    }


    componentDidMount() {
        this.props.get_headers()
            .then(result => this.setState({headers: result.data.Headers}))
            .catch(error => console.log(error));
    }

    generate_rows() {
        let rows;

        if (typeof this.props.data.rows == 'undefined') {
            rows = [];
        } else {
            rows = new Array(this.props.data.rows.length);
            this.props.data.rows.forEach(function (item, index) {
                rows[index] = item;
                rows[index].name = item.author
        });
        }
        return rows;
    }

    determine_header(header) {
        if(header in column_header_mappings){
            return column_header_mappings[header];
        } else {
            return header;
        }
    }

    format_data() {
        if (typeof this.props.data != 'undefined') {
            let rows = this.generate_rows(this.props.data);

            return (
                <tbody>
                {rows.map(row => (
                    <tr key={row.name}>
                        <td className={statBoxStyle.label}>
                            {row.name}
                        </td>
                        {this.state.headers.map(header => (
                            <td key={[header]} className={statBoxStyle.cell}>
                                {row.[header]}
                            </td>
                            )
                        )}
                    </tr>

                ))}
            </tbody>);

        } else {

            return ( <div/> );
        }
    }

    format_headers() {

        return (
            <tr>
                <th key={"blank"}> {' '} </th>
                {this.state.headers.map(header =>
                    <th className={statBoxStyle.header} key={header}>{this.determine_header(header)}</th>)}
            </tr>
        )


    }

    render() {
        return (
            <div className={statBoxStyle.box}>
                <Table className={statBoxStyle.table}>
                    <thead>
                        {this.format_headers()}
                    </thead>
                    {this.format_data()}
                </Table>
            </div>
        );
  }
}