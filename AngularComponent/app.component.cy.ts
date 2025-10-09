describe('AppComponent (Cypress E2E)', () => {
//   const URL = 'http://localhost:4200'; // o usa `Cypress.config().baseUrl`

  beforeEach(() => {
    cy.visit(URL);
  });

  it('debería multiplicar correctamente dos números', () => {
    cy.get('#num1').type('7');
    cy.get('#num2').type('6');
    cy.get('#btn').click();
    cy.get('#resultado')
      .should('be.visible')
      .and('contain.text', '42');
  });
});
