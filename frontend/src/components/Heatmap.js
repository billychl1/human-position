import React, { useEffect, useRef } from 'react';
import h337 from 'heatmap.js';
import axios from 'axios';

const Heatmap = ({ timeframe }) => {
    const heatmapRef = useRef(null);

    useEffect(() => {
        axios.get(`/api/heatmap?timeframe=${timeframe}`)
            .then(response => {
                const heatmapInstance = h337.create({
                    container: heatmapRef.current,
                    maxOpacity: 0.6,
                    radius: 50,
                    blur: 0.90,
                });
                heatmapInstance.setData({
                    max: 100,
                    data: response.data
                });
            })
            .catch(error => console.error(error));
    }, [timeframe]);

    return (
        <div ref={heatmapRef} style={{ width: '600px', height: '400px' }}></div>
    );
};

export default Heatmap;