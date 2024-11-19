import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const Graph = ({ selectedOption, timeframe }) => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get(`/api/data?option=${selectedOption}&timeframe=${timeframe}`)
            .then(response => setData(response.data))
            .catch(error => console.error(error));
    }, [selectedOption, timeframe]);

    const chartData = {
        labels: data.map(entry => new Date(entry.timestamp).toLocaleTimeString()),
        datasets: [
            {
                label: selectedOption,
                data: data.map(entry => entry.value),
                fill: false,
                borderColor: 'rgba(75,192,192,1)',
            },
        ],
    };

    return (
        <div>
            <Line data={chartData} />
        </div>
    );
};

export default Graph;