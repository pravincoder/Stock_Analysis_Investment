import React from 'react';

const Header = () => {
    return (
        <header style={styles.header}>
            <h1 style={styles.title}>Stock Investment & Analysis Agent</h1>
        </header>
    );
};

const styles = {
    header: {
        textAlign: 'center',
        padding: '40px',
        backgroundColor: '#1e3a8a',  // Dark blue background
        boxShadow: '0 4px 10px rgba(0, 0, 0, 0.1)',  // Adds a soft shadow
    },
    title: {
        fontSize: '3rem',  // Bigger font size for the title
        fontWeight: 'bold',
        color: '#ffffff',  // White color text
        letterSpacing: '2px',  // Slight letter spacing for a cleaner look
        textTransform: 'uppercase',  // Makes the title uppercase
    }
};

export default Header;
