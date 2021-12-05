import '../styles/globals.css';
import { ChakraProvider } from '@chakra-ui/react';
import { SWRConfig } from 'swr';

function MyApp({ Component, pageProps }) {
	return (
		<SWRConfig
			value={{
				fetcher: (resource, init) => fetch(resource, init).then((res) => res.json()),
			}}
		>
			<ChakraProvider>
				<Component {...pageProps} />
			</ChakraProvider>
		</SWRConfig>
	);
}

export default MyApp;
