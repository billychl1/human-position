import React, { useEffect, useState, useRef } from 'react';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import axios from 'axios';

const Graph = ({ selectedOption, timeframe }) => {
    const [data, setData] = useState([]);
    const chartRef = useRef(null);

    useEffect(() => {
        axios.get(`/api/data?option=${selectedOption}&timeframe=${timeframe}`)
            .then(response => setData(response.data))
            .catch(error => console.error(error));
    }, [selectedOption, timeframe]);

    useEffect(() => {
        const chartInstance = chartRef.current;
        if (chartInstance) {
            chartInstance.destroy();
        }

        const ctx = document.getElementById('myChart').getContext('2d');
        chartRef.current = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.map(entry => new Date(entry.timestamp).toLocaleTimeString()),
                datasets: [
                    {
                        label: selectedOption,
                        data: data.map(entry => entry.value),
                        fill: false,
                        borderColor: 'rgba(75,192,192,1)',
                    },
                ],
            },
        });
    }, [data]);

    return (
        <div>
            <canvas id="myChart"></canvas>
        </div>
    );
};

export default Graph;
