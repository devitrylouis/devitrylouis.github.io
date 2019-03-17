# Define the generator
class Encoder(nn.Module):
    def __init__(self, latent_n, layers):
        super().__init__()
        # Architecture
        self.layers = layers

        # Linear units + BatchNorm
        self.fc1 = nn.Linear(2, layers[0])
        self.bn1 = nn.BatchNorm1d(layers[0])

        self.fc2 = nn.Linear(layers[0], layers[1])
        self.bn2 = nn.BatchNorm1d(layers[1])

        # Non linear unit
        if activation == "leaky": self.activation = nn.LeakyReLU(0.2)
        else: self.activation = nn.ReLU()

        # Parameters unit
        self.fc_mu = nn.Linear(layers[-1], latent_n)
        self.fc_logvar = nn.Linear(layers[-1], latent_n)

    # encode a datapoint. This should return a couple of tensors (mu, logvar) representing
    # the parameters of the gaussian q_\phi(z | x)
    def __call__(self, x, leaky = False):

        h1 = self.activation(self.bn1(self.fc1(x)))
        h2 = self.activation(self.bn2(self.fc2(h1)))

        mu = self.fc_mu(h2)
        logvar = self.fc_logvar(h2)
        return (mu, logvar)


# Define the discriminator
class Decoder(nn.Module):
    def __init__(self, latent_n, layers):
        super().__init__()

        # Architecture
        self.layers = layers
        self.latent_n = latent_n

        # Linear units + BatchNorm
        self.fc1 = nn.Linear(latent_n, layers[0])
        self.bn1 = nn.BatchNorm1d(layers[0])

        self.fc2 = nn.Linear(layers[0], layers[1])
        self.bn2 = nn.BatchNorm1d(layers[1])

        # Non linear unit
        if activation == "leaky": self.activation = nn.LeakyReLU(0.2)
        else: self.activation = nn.ReLU()

        # Parameters unit
        self.fc_mu = nn.Linear(layers[-1], 2)
        self.fc_logvar = nn.Linear(layers[-1], 2)

    # decode a datapoint. This should return a couple of tensors (mu, logvar) representing
    # the parameters of the gaussian p_\theta(z | x)
    def __call__(self, z, leaky = False):

        h1 = self.activation(self.bn1(self.fc1(z)))
        h2 = self.activation(self.bn2(self.fc2(h1)))

        mu = self.fc_mu(h2)
        logvar = self.fc_logvar(h2)
        return (mu, logvar)

    def generate(self, batchlen):
        z = torch.normal(torch.zeros(batchlen, self.latent_n), 1.0)
        (mu, logvar) = self.__call__(z)
        return torch.normal(mu, torch.exp(0.5*logvar))
