import React, { useState } from 'react';
import Dropdown from './components/Dropdown';
import Graph from './components/Graph';
import Heatmap from './components/Heatmap';

const App = () => {
    const [selectedOption, setSelectedOption] = useState('Number of humans');
    const [timeframe, setTimeframe] = useState('1h');

    const options = ['Number of humans', 'X position of human'];

    return (
        <div>
            <Dropdown options={options} onChange={setSelectedOption} />
            <Graph selectedOption={selectedOption} timeframe={timeframe} />
            <Heatmap timeframe={timeframe} />
        </div>
    );
};

export default App;